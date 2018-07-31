# -*- coding: utf-8 -*-

# Add directories to PYTHONPATH for cron
import sys
sys.path.append('/home/dimau777/projects/eventer/')
sys.path.append('/home/dimau777/projects/eventer/eventer/')
sys.path.append('/home/dimau777/projects/eventer/eventer/model/')
sys.path.append('/home/dimau777/projects/eventer/eventer/utility/')
sys.path.append('/home/dimau777/projects/eventer/eventer/view/')
import time
import datetime
import requests
import copy
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from Event import Event


# Параметры для конфиг файла
user_for_mysql = "eventer"
password_for_mysql = "Nhgbf86jmnIK"

# Запуск сессии с базой данных
engine = sqlalchemy.create_engine("mysql://" + user_for_mysql + ":" + password_for_mysql + "@localhost/eventer?charset=utf8", echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class KudaGoParser:

    def main(self):
        """
        Метод скачивает списки событий (перебирает параметр page), и записывает новые данные в БД,
        пока не будет достигнут id последнего ранее успешно обработанного объявления
        :return:
        """
        last_handled_id_from_base = self.get_last_handled_id()

        page_number = 1
        old_event_in_collection = False
        while True:
            url = self.make_url(page=page_number)
            url_content = self.get_url_content(url)
            events_collection_source = self.list_parser(url_content)

            # Перебираем события из списка и формируем нормализованные словари под каждое отдельное событие
            events_collection_final = []
            for item in events_collection_source:
                if item['id'] <= int(last_handled_id_from_base):
                    old_event_in_collection = True
                    continue
                events = self.item_parser(item)
                events_collection_final += events

            # Remove events which have finished in past
            events_collection_final = self.remove_already_finished_events(events_collection_final)
            print("KudaGoParser:main(): page number: " + str(page_number) + " new events: " + str(len(events_collection_final)))

            # Новый набор событий с сайта записываем в базу
            self.write_events_to_db(events_collection_final)

            # Список событий отсортирован по убыванию id, если в новой выборке есть хотя бы 1 событие,
            # которое уже есть в базе, то дальше перебирать страницы нет смысла
            if old_event_in_collection or page_number == 500:
                break

            page_number = page_number + 1

            # Add sleep to don't ddos attack source server
            time.sleep(1)

    @staticmethod
    def get_last_handled_id():
        """
        Возвращает самый большой id_kudago из базы (последнее сохраненное в БД мероприятие с этого сайта)
        :return:
        """
        try:
            last_handled_id_tuple = session.query(Event._id_kudago).order_by(Event._id_kudago)[-1]
        except IndexError:
            last_handled_id_tuple = (0,)
        return last_handled_id_tuple[0]

    @staticmethod
    def make_url(page):
        """
        Собирает урл для получения страницы со списком мероприятий
        Url example: https://kudago.com/public-api/v1.4/events/?lang=ru&page_size=10&order_by=-id&text_format=html&location=msk&is_free=0&fields=id,dates,title,short_title,slug,place,description,body_text,location,categories, tagline,age_restriction,price,is_free,images,favorites_count,comments_count,site_url,tags,participants&page=1
        :return:
        """
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
            'fields': 'id,dates,title,short_title,slug,place,description,body_text,location,categories,tagline,age_restriction,price,is_free,images,favorites_count,comments_count,site_url,tags,participants',
            'page': page
        }
        return url

    @staticmethod
    def get_url_content(url):
        """
        Возвращает объект ответа с полным html текстом страницы (или JSON словарем) по переданному url
        :param url:
        :return:
        """
        # req = requests.get(url)
        with requests.get(url) as req:
            return req

    @staticmethod
    def list_parser(url_content):
        """
        Метод возвращает коллекцию из событий с данной страницы
        :return: 
        """
        url_content_json = url_content.json()
        return url_content_json['results']

    def item_parser(self, item):
        """
        Достает поля, нужные для сохранения события в БД
        :param item:
        :return: return list of events, in most cases it will contain only one item, but if event has several dates,
        every date will have its own event in list
        """
        events = []
        event_common_parameters = {}
        event_common_parameters['id_kudago'] = item['id']
        event_common_parameters['title'] = item['title']
        event_common_parameters['description'] = item['description']
        event_common_parameters['url'] = 'https://kudago.com/' + item['location']['slug'] + '/event/' + item['slug']
        event_common_parameters['categories_kudago'] = item['categories'][0]
        event_common_parameters['tags_kudago'] = item['tags']
        event_common_parameters['categories'] = self.type_of_event_converter(item['categories'][0])
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
            print("*********************************\n" + str(event))
        return events

    @staticmethod
    def type_of_event_converter(source_type_of_event):
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
            "holiday": ["holiday"],
            "social-activity": ["social-activity"],
            "yarmarki-razvlecheniya-yarmarki": ["yarmarki-razvlecheniya-yarmarki"],
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
            "ball": ["ball"],
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

    @staticmethod
    def remove_already_finished_events(events):
        result = []
        # TODO: refactoring 3 - will have be in config file
        current_timestamp = (datetime.datetime.now() + datetime.timedelta(hours=3)).timestamp() # server time is least for 3 hours than real moscow time
        for event in events:
            if event['finish_time'] > current_timestamp:
                result.append(event)
        return result

    @staticmethod
    def write_events_to_db(events_collection_normalized):
        # Запись всех новых событий в базу данных
        for item in events_collection_normalized:
            event = Event(item)
            session.add(event)
        session.commit()

        # Assignment real id of last event for duplicates of this event with other dates
        handled_duplicate_source_id = []
        for item in events_collection_normalized:
            if item['duplicate_source_id'] == "" or item['duplicate_source_id'] in handled_duplicate_source_id:
                continue
            all_duplicates = session.query(Event).filter(Event._duplicate_source_id == item['duplicate_source_id']).all()
            latest_event_id = sorted(all_duplicates, key=lambda x: x.start_time, reverse=True)[0].event_id
            for event in all_duplicates:
                event.duplicate_id = latest_event_id
                session.add(event)
                print(" ******************************** \n" + str(event))
            handled_duplicate_source_id.append(item['duplicate_source_id'])
        session.commit()
        return


if __name__ == '__main__':

    parser = KudaGoParser()
    parser.main()
