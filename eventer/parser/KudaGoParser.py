from AbstractParser import AbstractParser
from ParsingPointer import ParsingPointer
from Event import Event
from FormattingDataRepresentation import FormattingDataRepresentation
import copy
import logging
import re


class KudaGoParser(AbstractParser, FormattingDataRepresentation):

    def _create_parsing_pointer(self):
        parsing_pointer = ParsingPointer.get_parsing_pointer(source="KudaGo", session=self._session)
        return parsing_pointer

    def _check_parsing_pointer(self, event, previous_parsing_pointer_value):
        """
        Return True if this event is already in the database (publication_date of the event is less than parsing_pointer)
        Return False if this event is new (publication_date of the event is more than parsing_pointer)
        :param event:
        :param previous_parsing_pointer_value:
        :return:
        """
        logging.info('Enter to the method, publication_date of the event: %s, previous_parsing_pointer_value: %s',
                     event.publication_date, previous_parsing_pointer_value)
        if previous_parsing_pointer_value is None:
            return False
        if int(event.publication_date) > int(previous_parsing_pointer_value):
            return False
        return True

    def _new_parsing_pointer(self, event):
        return str(event.publication_date)

    def _make_url(self, page, test_url):
        """
        Making url for getting page with events
        Url example you can see at a test file
        :return:
        """
        logging.debug('Enter to the method')

        # For test running this method has to return giving test url (usually localhost url for test page)
        if test_url:
            return test_url + "&page=" + str(page)

        url_template = 'https://kudago.com/public-api/v1.4/events/?' \
                       'lang=%(lang)s&' \
                       'page_size=%(page_size)s&' \
                       'order_by=%(order_by)s&' \
                       'text_format=%(text_format)s&' \
                       'location=%(location)s&' \
                       'is_free=%(is_free)s&' \
                       'fields=%(fields)s&' \
                       'page=%(page)s'

        url = url_template % {
            'lang': 'ru',
            'page_size': '100',
            'order_by': "-publication_date",
            'text_format': 'html',
            'location': 'msk',
            'is_free': '0',
            'fields': 'id,publication_date,dates,title,short_title,slug,place,description,body_text,location,categories,tagline,age_restriction,price,is_free,images,favorites_count,comments_count,site_url,tags,participants',
            'page': page
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
        return url_content_json['results']

    def _item_parser(self, item):
        """
        Extract fields from source HTML or JSON to create Event from them
        :param item: part of source HTML or JSON which contains information about one event
        :return: return list of Events, in most cases it will contain only one item, but if event has several dates,
        every date will have its own Event in the list
        """
        logging.debug('Enter to the method, iter: %s', item)
        events = []

        event = Event()
        # If we cannot get this features (title and url) - we won't work with this event further
        try:
            event.title = item['title']
            event.url = 'https://kudago.com/' + item['location']['slug'] + '/event/' + item['slug']
            event.publication_date = item['publication_date']
        except KeyError:
            return []
        event.source = "KudaGo"
        event.id_kudago = item.get('id', None)
        event.description = item.get('description', None)
        event.categories_kudago = self.convert_from_iterator_to_string(item.get('categories', []))
        event.tags_kudago = item.get('tags', None)
        event.price_kudago = item.get('price', None)
        event.price_min, event.price_max = self._get_price_from_string(item.get('price', ""), item.get('is_free', ""))
        event.categories = item.get('categories', []) + item.get('tags', [])
        if len(item.get('images', [])) > 0:
            event.image = item['images'][0]['image']
        event.join_anytime = False

        # Complicate handling of dates
        dates = item.get('dates', [])
        if len(dates) > 1:
            # Firstly we will use unique identifier of the event - url
            # After saving to database we can use our own id
            event.duplicate_source_id = event.url
        for date_of_event in dates:
            event_for_date = copy.deepcopy(event)
            event_for_date.start_time = date_of_event['start']
            event_for_date.finish_time = date_of_event['end']
            events.append(event_for_date)
        if len(dates) == 0:
            event.start_time = 0
            event.finish_time = 0
            events.append(event)
        logging.debug('final list of events: %s', events)
        return events

    @staticmethod
    def _get_price_from_string(source_price_string, is_free):
        # Initialization
        price_min = None
        price_max = None
        if not source_price_string or not isinstance(source_price_string, str):
            return price_min, price_max

        # Like is_free == true
        if is_free:
            price_min = 0
            price_max = 0
            return price_min, price_max

        # Like "от 500 до 700 рублей" or "от 500 руб."
        result_of_matching = re.match("от (\d*).*", source_price_string)
        if result_of_matching and result_of_matching.group(1):
            price_min = int(result_of_matching.group(1))
            return price_min, price_max

        # Like "2000 рублей" or "2000 руб."
        result_of_matching = re.match("(\d*).*", source_price_string)
        if result_of_matching and result_of_matching.group(1):
            price_min = int(result_of_matching.group(1))
            price_max = price_min
            return price_min, price_max

        # Return result
        return price_min, price_max
