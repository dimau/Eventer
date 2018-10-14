from AbstractParser import AbstractParser
from FormattingDataRepresentation import FormattingDataRepresentation
from ParsingPointer import ParsingPointer
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

    def _new_parsing_pointer(self, event_dictionary):
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
                       'limit=20&' \
                       'offset=0&' \
                       'hasMixed=0&' \
                       'city=moscow'

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
        event_common_parameters = {}
        event_common_parameters['source'] = "YandexAfishaCinema"
        event_common_parameters['id_kudago'] = ""
        event_common_parameters['publication_date'] = ""
        event_common_parameters['title'] = item['event']['title']
        event_common_parameters['description'] = item['event']['argument']
        event_common_parameters['url'] = 'https://afisha.yandex.ru' + item['event']['url']
        event_common_parameters['categories_kudago'] = ""
        event_common_parameters['tags_kudago'] = []
        event_common_parameters['price_kudago'] = ""
        event_common_parameters['price_min'], event_common_parameters['price_max'] = None, None
        event_common_parameters['categories'] = self.convert_from_iterator_to_string(self._get_all_categories(item['event']['systemTags']))
        event_common_parameters['image'] = item['event']['image']['eventCover']['url']
        # Now we write to the DB not all sessions with every film (too much every day) but only days
        # when this film is on screens in cinemas
        event_common_parameters['join_anytime'] = True

        # Complicate handling of dates
        if len(item['scheduleInfo']['dates']) > 1:
            # Firstly we will use unique identifier of the event - url
            # After saving to database we can use our own id
            event_common_parameters['duplicate_source_id'] = event_common_parameters['url']
        else:
            event_common_parameters['duplicate_source_id'] = ""
        for date_of_event in item['scheduleInfo']['dates']:
            event = copy.deepcopy(event_common_parameters)
            date_parts = date_of_event.split('-')  # date_of_event = "2018-10-14"
            event['start_time'] = datetime.datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2])).timestamp()
            event['finish_time'] = event['start_time'] + 86399  # one full day in seconds without 1 second
            events.append(event)
        if len(item['scheduleInfo']['dates']) == 0:
            event = copy.deepcopy(event_common_parameters)
            event['start_time'] = 0
            event['finish_time'] = 0
            events.append(event)
        logging.debug('final list of dictionaries: %s', events)
        return events

    @staticmethod
    def _get_all_categories(source_list):
        categories = set('cinema')
        for item in source_list:
            categories.add(item['code'])
        return categories
