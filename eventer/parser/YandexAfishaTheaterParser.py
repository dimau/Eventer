from AbstractParser import AbstractParser
from FormattingDataRepresentation import FormattingDataRepresentation
from ParsingPointer import ParsingPointer
from Event import Event
import logging
import copy
import datetime
from bs4 import BeautifulSoup
import re


class YandexAfishaTheaterParser(AbstractParser, FormattingDataRepresentation):

    def _create_parsing_pointer(self):
        parsing_pointer = ParsingPointer.get_parsing_pointer(source="YandexAfishaTheater", session=self._session)
        return parsing_pointer

    def _check_parsing_pointer(self, event_dictionary, previous_parsing_pointer_value):
        """
        This parser really works only in "full" mode, but if anybody starts it in "only_new" mode we have
        don't write any event to database because it can duplicate existing events in the database
        Return True if this event is already in the database (publication_date of the event is less than parsing_pointer)
        Return False if this event is new (publication_date of the event is more than parsing_pointer)
        :param event_dictionary:
        :param previous_parsing_pointer_value:
        :return:
        """
        return True

    def _new_parsing_pointer(self, event):
        return "dummy"

    def _make_url(self, page, test_url):
        """
        Making url for getting page with events
        :return: string with url
        """
        logging.debug('Enter to the method')

        # For test running this method has to return giving test url (usually localhost url for test page)
        if test_url:
            return test_url + "&page=" + str(page)

        url_template = 'https://afisha.yandex.ru/api/events/selection/all-events-theatre?' \
                       'limit=%(limit)s&' \
                       'offset=%(offset)s&' \
                       'hasMixed=%(hasMixed)s&' \
                       'city=%(city)s'

        url = url_template % {
            'limit': '20',
            'offset': page * 20 - 20,
            'hasMixed': "0",
            'city': 'moscow'
        }

        logging.info('Url for parsing: %s', url)
        return url

    def _list_parser(self, url_content):
        """
        Getting list of events from giving page content
        :param url_content: object of response from requests.get(url)
        :return: list of events in JSON or None
        """
        logging.debug('Enter to the method')
        try:
            url_content_json = url_content.json()
        except Exception as e:
            logging.error("Bad url content: %s error: %s", url_content, e)
            return None
        list_with_results = url_content_json.get('data', [])
        logging.info('We have extracted from page in our list %s events', len(list_with_results))
        return list_with_results

    def _item_parser(self, item):
        """
        Extract fields from source HTML or JSON to create Event from them and save to database
        :param item:
        :return: return list of events, in most cases it will contain only one item, but if event has several dates,
        every date will have its own event in list
        """
        logging.debug('Enter to the method, iter: %s', item)
        events = []

        event = Event()
        # If we cannot get this features (title and url) - we won't work with this event further
        try:
            event.title = item['event']['title']
            event.url = 'https://afisha.yandex.ru' + item['event']['url']
        except KeyError:
            return []
        event.source = "YandexAfishaTheater"
        event.description = item.get('event', {}).get('argument', None)
        event.categories = self._get_all_categories(item.get('event', {}).get('systemTags', []))
        event.image = item.get('event', {}).get('image', {}).get('eventCover', {}).get('url', None)
        event.join_anytime = False
        event.status = "active"
        event.price_min, event.price_max = self._get_price_from_json(item)

        # We have get a page of this event and extract time for every date
        times = self._get_times_of_event(event.url)
        print(str(times))

        # Complicate handling of dates
        dates = item.get('scheduleInfo', {}).get('dates', [])
        if len(dates) > 1:
            # Firstly we will use unique identifier of the event - url
            # After saving to database we can use our own id
            event.duplicate_source_id = event.url
        for date_of_event in dates:
            event_for_date = copy.deepcopy(event)
            date_parts = date_of_event.split('-')  # date_of_event = "2018-10-14"
            event_for_date.start_time = int(datetime.datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]), tzinfo=datetime.timezone.utc).timestamp())
            event_for_date.finish_time = event_for_date.start_time + 86400 - 1  # one full day in seconds without 1 second
            events.append(event_for_date)
        if len(dates) == 0:
            event.start_time = 0
            event.finish_time = 0
            events.append(event)
        logging.debug('Events after item parsing: %s', events)
        return events

    @staticmethod
    def _get_all_categories(source_list):
        categories = set()
        categories.add("theater")
        for item in source_list:
            categories.add(item['code'])
        return categories

    @staticmethod
    def _get_price_from_json(item):
        # Initialization
        price_min = None
        price_max = None

        try:
            price_min = item['event']['tickets'][0]['price']['min']
            price_min = int(int(price_min) / 100)
        except (KeyError, IndexError):
            price_min = None

        try:
            price_max = item['event']['tickets'][0]['price']['max']
            price_max = int(int(price_max) / 100)
        except (KeyError, IndexError):
            price_max = None

        # Return result
        return price_min, price_max

    def _get_times_of_event(self, url):
        """
        This method extracting concrete times of the beginning the event for every date and duration of the event.
        Return list of tuples like (date, start_time, finish_time) or [] if something goes wrong
        :param url:
        :return: example: ()
        """
        all_dates_and_times = []

        # Getting of the HTML content for url
        url_content = self._get_url_content(url)
        if url_content.status_code != 200:
            return all_dates_and_times
        content_text = url_content.text
        soup = BeautifulSoup(content_text)

        # Extracting of the duration of the event
        try:
            duration = soup.find('dt', class_='event-attributes__category', text="Время").parent.find('dd', class_='event-attributes__category-value').text
            duration = re.search(r'\d+', duration).group()
            duration = int(duration) * 60  # Convert from minutes to seconds
        except AttributeError as e:
            duration = 0

        # Extracting dates and times for the event
        all_dates_source = soup.find_all('div', class_='schedule-other-list__item')
        try:
            for day in all_dates_source:
                date_date = day.find('div', class_='schedule-date__date').text
                date_month = self._convert_month_to_int(day.find('div', class_='schedule-date__month').text)
                date_time = day.find('div', class_='schedule-session').text
                all_dates_and_times.append((date_date + "-" + date_month, date_time, date_time + duration))
        except AttributeError as e:
            all_dates_and_times = []

        return all_dates_and_times

    @staticmethod
    def _convert_month_to_int(month):
        source_month = str(month)
        converter = {
            "января": "1",
            "февраля": "2",
            "марта": "3",
            "апреля": "4",
            "мая": "5",
            "июня": "6",
            "июля": "7",
            "августа": "8",
            "сентября": "9",
            "октября": "10",
            "ноября": "11",
            "декабря": "12"
        }
        return converter.get(source_month, None)

    def _inactivate_not_represented_on_source_events(self, all_events_ids):
        outdated_events = self._session.query(Event).filter(Event._source == "YandexAfishaTheater").filter(~Event._id.in_(all_events_ids))
        for event in outdated_events:
            event.status = "hidden"
            self._session.add(event)
        self._session.commit()
