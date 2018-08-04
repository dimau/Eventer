from AbstractParser import AbstractParser
from ParsingPointer import ParsingPointer
import copy
import logging
import re


class KudaGoParser(AbstractParser):

    def _create_parsing_pointer(self):
        parsing_pointer = ParsingPointer.get_parsing_pointer(source="KudaGo", session=self._session)
        return parsing_pointer

    def _check_parsing_pointer(self, event_dictionary, previous_parsing_pointer_value):
        logging.info('Enter to the method, item["publication_date"]: %s, previous_parsing_pointer_value: %s', event_dictionary['publication_date'], previous_parsing_pointer_value)
        if previous_parsing_pointer_value is None:
            return False
        if int(event_dictionary['publication_date']) > int(previous_parsing_pointer_value):
            return False
        return True

    def _new_parsing_pointer(self, event_dictionary):
        return str(event_dictionary["publication_date"])

    def _make_url(self, page):
        """
        Собирает урл для получения страницы со списком мероприятий
        Url example: https://kudago.com/public-api/v1.4/events/?lang=ru&page_size=10&order_by=-id&text_format=html&location=msk&is_free=0&fields=id,dates,title,short_title,slug,place,description,body_text,location,categories, tagline,age_restriction,price,is_free,images,favorites_count,comments_count,site_url,tags,participants&page=1
        :return:
        """
        logging.debug('Enter to the method')
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
            'page_size': '10',
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
        Метод возвращает коллекцию из событий с данной страницы
        :return: 
        """
        logging.debug('Enter to the method')
        url_content_json = url_content.json()
        return url_content_json['results']

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
        event_common_parameters['id_kudago'] = item['id']
        event_common_parameters['publication_date'] = item['publication_date']
        event_common_parameters['title'] = item['title']
        event_common_parameters['description'] = item['description']
        event_common_parameters['url'] = 'https://kudago.com/' + item['location']['slug'] + '/event/' + item['slug']
        event_common_parameters['categories_kudago'] = item['categories'][0]
        event_common_parameters['tags_kudago'] = item['tags']
        event_common_parameters['price_kudago'] = item['price']
        event_common_parameters['price_min'], event_common_parameters['price_max'] = self._get_price_from_string(item['price'])
        event_common_parameters['categories'] = self._type_of_event_converter(item['categories'][0])
        if len(item['images']) > 0:
            event_common_parameters['image'] = item['images'][0]['image']
        else:
            event_common_parameters['image'] = ""
        if len(item['dates']) > 1:
            event_common_parameters['duplicate_source_id'] = event_common_parameters['id_kudago']  # Пока положим сюда id из сайта источника - kuda go, после сохранения в базу нужно будет взять наш собственный индекс
        else:
            event_common_parameters['duplicate_source_id'] = ""
        for date_of_event in item['dates']:
            event = copy.deepcopy(event_common_parameters)
            event['start_time'] = date_of_event['start']
            event['finish_time'] = date_of_event['end']
            events.append(event)
        logging.debug('final list of dictionaries: %s', events)
        return events

    @staticmethod
    def _get_price_from_string(source_price_string):
        # Initialization
        price_min = None
        price_max = None
        if not source_price_string or not isinstance(source_price_string, str):
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

    @staticmethod
    def _type_of_event_converter(source_type_of_event):
        type_of_event_dictionary = {
            "concert": ["concert"],
            "theater": ["theater"],
            "education": ["education"],
            "party": ["party"],
            "sport": ["sport"],
            "exhibition": ["exhibition"],
            "tour": ["tour"],
            "festival": ["festival"],
            "cinema": ["cinema"],
            "fashion": ["fashion"],
            "show": ["show"],
            "holiday": ["festival"],
            "social-activity": ["social-activity"],
            "yarmarki-razvlecheniya-yarmarki": ["festival"],
            "games": ["games"],
            "night": ["night"],
            "meeting": ["meeting"],
            "speed-dating": ["speed-dating"],
            "flashmob": ["flashmob"],
            "masquerade": ["masquerade"],
            "romance": ["romance"],
            "dance-trainings": ["dance-trainings"],
            "evening": ["evening"],
            "discount": ["discount"],
            "stock": ["stock"],
            "sale": ["sale"],
            "shopping": ["shopping"],
            "quest": ["quest"],
            "ball": ["festival"],
            "yoga": ["yoga"],
            "presentation": ["presentation"],
            "magic": ["magic"],
            "kvn": ["kvn"],
            "comedy-club": ["comedy-club"],
            "stand-up": ["stand-up"],
            "kids": ["kids"],
            "circus": ["circus"],
            "open": ["open"],
            "other": ["other"],
            "photo": ["photo"],
            "global": ["global"],
            "permanent-exhibitions": ["permanent-exhibitions"],
            "business-events": ["business-events"]
        }
        return set(type_of_event_dictionary.get(source_type_of_event, []))
