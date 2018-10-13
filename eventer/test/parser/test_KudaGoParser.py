import pytest
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from Base_class_sql_alchemy import Base
from KudaGoParser import KudaGoParser
from Event import Event
from User import User
from Rating import Rating
from ParsingPointer import ParsingPointer


class TestKudaGoParser:

    # We create a new clear database and session to it only one time for all test cases in this class
    @pytest.fixture(scope="class")
    def session(self):
        engine = sqlalchemy.create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        yield session
        session.close()

    # We use this fixture in the beginning of every test case for clearing all tables in database in memory
    @pytest.fixture()
    def clear_data(self, session):
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()

    def test_parsing_page_with_one_event(self, session, clear_data):
        parsing_pointer = ParsingPointer.get_parsing_pointer(source="KudaGo", session=session)
        parsing_pointer.current_pointer = "123456"
        session.add(parsing_pointer)
        session.commit()
        event = Event({"title": "выставка Face 2 Face",
                       "description": "<p>Хотите лицом к лицу встретиться с героями известных фильмов? Добро пожаловать в фантастическое пространство Face 2 Face, где реальность переплетена с вымыслом.</p>",
                       "id_kudago": "173791",
                       "categories_kudago": "exhibition|kids",
                       "tags_kudago": ["интерактивные", "новые технологии", "детские", "новое на сайте", "выставки",
                                       "детские (раздел детям)", "всей семьей", "фэнтези", "интересное",
                                       "выходные с детьми"],
                       "price_kudago": "от 0 до 650 рублей",
                       "url": "https://kudago.com/msk/event/vyistavka-face-2-face",
                       "categories": ["exhibition", "kids"],
                       "image": "https://kudago.com/media/images/event/e1/6f/e16fa25bbf494ca18def9aa9580a5f5f.JPG",
                       "start_time": 1539421200,
                       "finish_time": 1543777200,
                       "duplicate_source_id": '',
                       "duplicate_id": 0,
                       "price_min": 0,
                       "price_max": None
                       })
        parser = KudaGoParser(session)
        assert parser.main(test_url="http://127.0.0.1:5000?source=kudago&testcase=one_event") == 2
        event_from_db = session.query(Event).first()
        self.check_equivalence_of_two_events(event, event_from_db)

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

    def test_make_url_for_first_page(self, session, clear_data):
        parser = KudaGoParser(session)
        assert parser._make_url(page=1,
                                test_url=None) == "https://kudago.com/public-api/v1.4/events/?lang=ru&page_size=100&order_by=-publication_date&text_format=html&location=msk&is_free=0&fields=id,publication_date,dates,title,short_title,slug,place,description,body_text,location,categories,tagline,age_restriction,price,is_free,images,favorites_count,comments_count,site_url,tags,participants&page=1"

    def test_make_url_with_test_url(self, session, clear_data):
        parser = KudaGoParser(session)
        assert parser._make_url(page=1, test_url="http://127.0.0.1:5000?source=kudago&testcase=404") == "http://127.0.0.1:5000?source=kudago&testcase=404&page=1"

    def test_parsing_page_with_404_status_code(self, session, clear_data):
        parser = KudaGoParser(session)
        assert parser.main(test_url="http://127.0.0.1:5000?source=kudago&testcase=404") == 1
        events_from_db = session.query(Event).all()
        assert [] == events_from_db

    def check_equivalence_of_two_events(self, event1, event2):
        assert event1._title == event2._title
        assert event1._description == event2._description
        assert event1._id_kudago == event2._id_kudago
        assert event1._categories_kudago == event2._categories_kudago
        assert event1._tags_kudago == event2._tags_kudago
        assert event1._price_kudago == event2._price_kudago
        assert event1._url == event2._url
        assert event1._categories.split("|").sort() == event2._categories.split("|").sort()
        assert event1._image == event2._image
        assert event1._start_time == event2._start_time
        assert event1._finish_time == event2._finish_time
        assert event1._duplicate_source_id == event2._duplicate_source_id
        assert event1._duplicate_id == event2._duplicate_id
        assert event1._price_min == event2._price_min
        assert event1._price_max == event2._price_max
