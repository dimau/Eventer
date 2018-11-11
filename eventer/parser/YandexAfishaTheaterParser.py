from AbstractParser import AbstractParser
from FormattingDataRepresentation import FormattingDataRepresentation
from ParsingPointer import ParsingPointer
from Event import Event
import logging
import copy
import datetime


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

    def _item_parser(self, item, test_url=None):
        """
        Extract fields from source HTML or JSON to create Event from them and save to database
        :param item:
        :param test_url: uses if method have download additional data from the page of concrete event and parse it
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
        except (KeyError, AttributeError):
            return []
        # This extracting can spawn an exception
        try:
            event.description = item.get('event', {}).get('argument', None)
            event.categories = self._get_all_categories(item.get('event', {}).get('systemTags', []))
            event.image = item.get('event', {}).get('image', {}).get('eventCover', {}).get('url', None)
            event.source_rating_value = item.get('event', {}).get('userRating', {}).get('overall', {}).get('value', None)
            event.source_rating_count = item.get('event', {}).get('userRating', {}).get('overall', {}).get('count', None)
        except (KeyError, AttributeError):
            pass
        event.source = "YandexAfishaTheater"
        event.status = "active"
        event.join_anytime = False
        event.price_min, event.price_max = self._get_price_from_json(item)

        # We have one more url request for this event and extracting start_times for every date
        yandex_event_id = item.get('event', {}).get('id', None)
        start_times = self._get_start_times_of_the_event(yandex_event_id, test_url=test_url)

        # Complicate handling of dates
        if len(start_times) > 1:
            # Firstly we will use unique identifier of the event - url
            # After saving to database we can use our own id
            event.duplicate_source_id = event.url
        for start_time_of_event in start_times:
            event_session = copy.deepcopy(event)
            event_session.start_time = start_time_of_event
            event_session.finish_time = start_time_of_event
            events.append(event_session)
        if len(start_times) == 0:
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

    def _get_start_times_of_the_event(self, yandex_event_id, test_url):
        """
        This method extracting concrete times of the beginning of the event for every date.
        Return list of timestamps in UTC or [] if something goes wrong
        :param yandex_event_id: this parameter uses for making url for getting data
        :param test_url: url for data for using in testing purposes
        :return:
        """
        logging.debug('Enter to the method')
        all_start_times = []

        # Getting the JSON content for yandex_event_id about dates and times
        # Example of the url for event:
        # https://afisha.yandex.ru/api/events/5b61991392ced5d88d7e5f69/schedule_other?date=2018-11-11&period=180&city=moscow
        url = 'https://afisha.yandex.ru/api/events/{0}/schedule_other?date={1}&period=180&city={2}'.format(
            yandex_event_id, datetime.date.today().isoformat(), "moscow")
        if test_url:
            url = test_url + "&event_source_id=" + str(yandex_event_id)
        url_content = self._get_url_content(url)
        if url_content.status_code != 200:
            return all_start_times

        # List parser
        try:
            url_content_json = url_content.json()
        except Exception as e:
            logging.error("Bad url content: %s error: %s", url_content, e)
            return all_start_times
        list_with_dates_data = url_content_json.get('schedule', {}).get('items', [])
        logging.debug('We have extracted from page in our list %s events', len(list_with_dates_data))

        # Extracting timestamps of beginnings for the event
        for day in list_with_dates_data:
            for session in day.get('sessions', []):
                item = session.get('session', {}).get('datetime', None)  # 2018-11-11T13:00:00
                if item is None:
                    continue
                item = int(datetime.datetime.strptime(item, "%Y-%m-%dT%H:%M:%S").timestamp())
                all_start_times.append(item)
        return all_start_times

    def _inactivate_not_represented_on_source_events(self, all_events_ids):
        outdated_events = self._session.query(Event).filter(Event._source == "YandexAfishaTheater").filter(~Event._id.in_(all_events_ids))
        for event in outdated_events:
            event.status = "hidden"
            self._session.add(event)
        self._session.commit()
