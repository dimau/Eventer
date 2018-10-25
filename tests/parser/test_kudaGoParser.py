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
