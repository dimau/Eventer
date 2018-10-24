from AbstractParser import AbstractParser
from FormattingDataRepresentation import FormattingDataRepresentation
from ParsingPointer import ParsingPointer
from Event import Event
import logging
import copy
import datetime


class YandexAfishaCinemaParser(AbstractParser, FormattingDataRepresentation):

    def _create_parsing_pointer(self):
        parsing_pointer = ParsingPointer.get_parsing_pointer(source="YandexAfishaCinema", session=self._session)
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

        url_template = 'https://afisha.yandex.ru/api/events/selection/all-events-cinema?' \
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
        return url_content_json['data']

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
        event.source = "YandexAfishaCinema"
        event.description = item.get('event', {}).get('argument', None)
        event.categories = self._get_all_categories(item.get('event', {}).get('systemTags', []))
        event.image = item.get('event', {}).get('image', {}).get('eventCover', {}).get('url', None)
        # Now we write to the DB not all sessions with every film (too much every day) but only days
        # when this film is on screens in cinemas
        event.join_anytime = True
        event.status = "active"

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
        logging.debug('final list of events: %s', events)
        return events

    @staticmethod
    def _get_all_categories(source_list):
        categories = set()
        categories.add("cinema")
        for item in source_list:
            categories.add(item['code'])
        return categories

    def _inactivate_not_represented_on_source_events(self, all_events_ids):
        outdated_events = self._session.query(Event).filter(Event._source == "YandexAfishaCinema").filter(~Event._id.in_(all_events_ids))
        for event in outdated_events:
            event.status = "hidden"
            self._session.add(event)
        self._session.commit()
