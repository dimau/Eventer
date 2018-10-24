from AbstractTestClass import AbstractTestClass
from KudaGoParser import KudaGoParser
from Event import Event
from User import User
from Rating import Rating
from ParsingPointer import ParsingPointer


class TestKudaGoParser(AbstractTestClass):

    def test_parsing_page_with_one_event(self, session, clear_data):
        parsing_pointer = ParsingPointer.get_parsing_pointer(source="KudaGo", session=session)
        parsing_pointer.current_pointer = "123456"
        session.add(parsing_pointer)
        session.commit()
        event = Event()
        event.source = "KudaGo"
        event.title = "выставка Face 2 Face"
        event.description = "<p>Хотите лицом к лицу встретиться с героями известных фильмов? Добро пожаловать в фантастическое пространство Face 2 Face, где реальность переплетена с вымыслом.</p>"
        event.price_kudago = "от 0 до 650 рублей"
        event.url = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event.categories = {"exhibition", "kids", "интерактивные", "новые технологии", "детские", "новое на сайте", "выставки", "детские (раздел детям)", "всей семьей", "фэнтези", "интересное", "выходные с детьми"}
        event.image = "https://kudago.com/media/images/event/e1/6f/e16fa25bbf494ca18def9aa9580a5f5f.JPG"
        event.start_time = 4695469200
        event.finish_time = 4699825200
        event.join_anytime = False
        event.price_min = 0
        event.status = "active"
        parser = KudaGoParser(session)
        assert parser.main(test_url="http://127.0.0.1:5000?source=kudago&testcase=one_event") == 2
        event_from_db = session.query(Event).first()
        self.check_equivalence_of_two_events(event, event_from_db)

    def test_parsing_only_old_event_on_the_first_page_in_only_new_mode(self, session, clear_data):
        parsing_pointer = ParsingPointer.get_parsing_pointer(source="KudaGo", session=session)
        parsing_pointer.current_pointer = "1539356260"
        session.add(parsing_pointer)
        session.commit()
        parser = KudaGoParser(session)
        assert parser.main(mode='only_new',
                           test_url="http://127.0.0.1:5000?source=kudago&testcase=only_old_event_on_the_first_page_in_only_new_mode") == 1
        events_from_db = session.query(Event).all()
        assert len(events_from_db) == 0

    def test_parsing_four_pages_in_full_mode(self, session, clear_data):
        """
        This test case is about full mode
        The first page has only one event
        The second page has the same only one event
        The third page has two events - the same one and the new one
        The fourth page is 404
        Totally we have 2 events and 4 pages for parsing
        :param session:
        :param clear_data:
        :return:
        """
        parsing_pointer = ParsingPointer.get_parsing_pointer(source="KudaGo", session=session)
        parsing_pointer.current_pointer = "1539356260"
        session.add(parsing_pointer)
        session.commit()
        parser = KudaGoParser(session)
        assert parser.main(mode='full', test_url="http://127.0.0.1:5000?source=kudago&testcase=four_pages_in_full_mode") == 4
        events_from_db = session.query(Event).all()
        assert len(events_from_db) == 2

    def test_parsing_page_with_bad_json_format_in_full_mode(self, session, clear_data):
        parser = KudaGoParser(session)
        assert parser.main(mode='full',
                           test_url="http://127.0.0.1:5000?source=kudago&testcase=page_with_bad_json_format") == 1
        events_from_db = session.query(Event).all()
        assert len(events_from_db) == 0

    def test_parsing_page_with_404_status_code(self, session, clear_data):
        parser = KudaGoParser(session)
        assert parser.main(test_url="http://127.0.0.1:5000?source=kudago&testcase=404") == 1
        events_from_db = session.query(Event).all()
        assert [] == events_from_db

    def test_make_url_for_second_page(self, session, clear_data):
        parser = KudaGoParser(session)
        assert parser._make_url(page=2,
                                test_url=None) == "https://kudago.com/public-api/v1.4/events/?lang=ru&page_size=100&order_by=-publication_date&text_format=html&location=msk&is_free=0&fields=id,publication_date,dates,title,short_title,slug,place,description,body_text,location,categories,tagline,age_restriction,price,is_free,images,favorites_count,comments_count,site_url,tags,participants&page=2"

    def test_make_url_with_test_url(self, session, clear_data):
        parser = KudaGoParser(session)
        assert parser._make_url(page=1, test_url="http://127.0.0.1:5000?source=kudago&testcase=404") == "http://127.0.0.1:5000?source=kudago&testcase=404&page=1"

    def test_update_events_from_db(self, session, clear_data):
        event_from_database_for_updating = Event()
        event_from_source_for_updating = Event()
        event_from_database_for_inactivating = Event()
        event_from_source_for_adding = Event()
        events = [event_from_source_for_updating, event_from_source_for_adding]
        same_events_in_db = [event_from_database_for_updating, event_from_database_for_inactivating]

        event_from_database_for_updating._id = 78
        event_from_database_for_updating.source = "KudaGo"
        event_from_database_for_updating.title = "выставка Face 2 Face"
        event_from_database_for_updating.description = "Хотите лицом к лицу встретиться с героями известных фильмов? Добро пожаловать"
        event_from_database_for_updating.price_kudago = "от 0 до 650 рублей"
        event_from_database_for_updating.url = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event_from_database_for_updating.categories = {"exhibition", "kids", "интерактивные", "новые технологии"}
        event_from_database_for_updating.image = "https://kudago.com/media/images/event/e1/6f/a5f5f.JPG"
        event_from_database_for_updating.start_time = 4695469200
        event_from_database_for_updating.finish_time = 4699825200
        event_from_database_for_updating.join_anytime = False
        event_from_database_for_updating.duplicate_source_id = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event_from_database_for_updating.duplicate_id = 45
        event_from_database_for_updating.price_min = 0
        event_from_database_for_updating.price_max = 25
        event_from_database_for_updating.status = "active"

        event_from_source_for_updating.source = "KudaGo"
        event_from_source_for_updating.title = "Обсуждение фильма Хоррор"
        event_from_source_for_updating.description = "Вот уж точно фильм, от которого волосы встают дыбом"
        event_from_source_for_updating.price_kudago = "500 рублей"
        event_from_source_for_updating.url = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event_from_source_for_updating.categories = {"интересненькое", "опера"}
        event_from_source_for_updating.image = "https://kudago.com/media/images/event/e1/6f/5f.JPG"
        event_from_source_for_updating.start_time = 4695469200
        event_from_source_for_updating.finish_time = 4699825200
        event_from_source_for_updating.join_anytime = True
        event_from_source_for_updating.duplicate_source_id = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event_from_source_for_updating.duplicate_id = 0
        event_from_source_for_updating.price_min = 500
        event_from_source_for_updating.price_max = 500
        event_from_source_for_updating.status = "active"

        event_from_database_for_inactivating._id = 80
        event_from_database_for_inactivating.source = "KudaGo"
        event_from_database_for_inactivating.url = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event_from_database_for_inactivating.start_time = 4695469500
        event_from_database_for_inactivating.finish_time = 4699825500
        event_from_database_for_inactivating.duplicate_source_id = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event_from_database_for_inactivating.duplicate_id = 45
        event_from_database_for_inactivating.status = "active"

        event_from_source_for_adding.source = "KudaGo"
        event_from_source_for_adding.url = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event_from_source_for_adding.start_time = 4695469900
        event_from_source_for_adding.finish_time = 4699825900
        event_from_source_for_adding.duplicate_source_id = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event_from_source_for_adding.duplicate_id = 0
        event_from_source_for_adding.status = "active"

        result_list_of_events = KudaGoParser._update_events_from_db(same_events_in_db, events)
        self.check_equivalence_of_two_events(result_list_of_events[0], event_from_source_for_updating)
        self.check_equivalence_of_two_events(result_list_of_events[1], event_from_source_for_adding)
        event_from_database_for_inactivating.status = "active"
        self.check_equivalence_of_two_events(result_list_of_events[2], event_from_database_for_inactivating)
