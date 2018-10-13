import pytest
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from Base_class_sql_alchemy import Base
from KudaGoParser import KudaGoParser
from Event import Event
from User import User
from Rating import Rating
from ParsingPointer import ParsingPointer


@pytest.fixture(scope="module")
def session():
    engine = sqlalchemy.create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def test_parsing_page_with_one_event(session):
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
    parser.main(test_url="http://127.0.0.1:5000/kudago_one_event/")
    event_from_db = session.query(Event).first()
    check_equlity_of_two_events(event, event_from_db)


def test_make_url_for_first_page(session):
    parser = KudaGoParser(session)
    assert parser._make_url(page=1,
                            test_url=None) == "https://kudago.com/public-api/v1.4/events/?lang=ru&page_size=100&order_by=-publication_date&text_format=html&location=msk&is_free=0&fields=id,publication_date,dates,title,short_title,slug,place,description,body_text,location,categories,tagline,age_restriction,price,is_free,images,favorites_count,comments_count,site_url,tags,participants&page=1"


def test_make_url_with_test_url(session):
    parser = KudaGoParser(session)
    assert parser._make_url(page=1, test_url="http://127.0.0.1:5000/kudago1/") == "http://127.0.0.1:5000/kudago1/"


def check_equlity_of_two_events(event1, event2):
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
