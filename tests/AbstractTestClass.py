import pytest
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from Base_class_sql_alchemy import Base
from Event import Event


class AbstractTestClass:

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

    @staticmethod
    def check_equivalence_of_two_events(event1, event2):
        assert event1.source == event2.source
        assert event1.title == event2.title
        assert event1.description == event2.description
        assert event1.price_kudago == event2.price_kudago
        assert event1.url == event2.url
        assert event1.categories == event2.categories
        assert event1.image == event2.image
        assert event1.start_time == event2.start_time
        assert event1.finish_time == event2.finish_time
        assert event1.join_anytime == event2.join_anytime
        assert event1.duplicate_source_id == event2.duplicate_source_id
        assert event1.duplicate_id == event2.duplicate_id
        assert event1.price_min == event2.price_min
        assert event1.price_max == event2.price_max
        assert event1.status == event2.status

    @staticmethod
    def create_event_kudago_exhibition_face2face():
        event = Event()
        event.source = "KudaGo"
        event.title = "выставка Face 2 Face"
        event.description = "<p>Хотите лицом к лицу встретиться с героями известных фильмов?</p>"
        event.price_kudago = "от 0 до 650 рублей"
        event.url = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event.categories = {"exhibition", "kids", "интерактивные", "новые технологии", "детские", "новое на сайте",
                            "выставки", "детские (раздел детям)", "всей семьей", "фэнтези", "интересное",
                            "выходные с детьми"}
        event.image = "https://kudago.com/media/images/event/e1/6f/e16fa25bbf494ca18def9aa9580a5f5f.JPG"
        event.start_time = 4695469200
        event.finish_time = 4699825200
        event.join_anytime = False
        event.price_min = 0
        event.status = "active"
        return event

    @staticmethod
    def create_event_yandexafishacinema_cinema_venom(start_time=4695148800, finish_time=4695235199, duplicate_id=None):
        event = Event()
        event.source = "YandexAfishaCinema"
        event.title = "Веном"
        event.description = "С участием Вуди Харрельсона"
        event.url = "https://afisha.yandex.ru/moscow/cinema/venom-2018"
        event.categories = {"thriller", "adventure", "fiction", "action", "horror", "cinema"}
        event.image = "https://afisha.yandex.ru/13Iaf1251.jpg"
        event.start_time = start_time
        event.finish_time = finish_time
        event.join_anytime = True
        event.duplicate_id = duplicate_id
        event.status = "active"
        return event

    @staticmethod
    def create_event_yandexafishatheater_theater_beshenyedengi(start_time=4695148800, finish_time=4695235199, duplicate_id=None):
        event = Event()
        event.source = "YandexAfishaTheater"
        event.title = "Бешеные деньги"
        event.description = "В главной роли Светлана Немоляева"
        event.url = "https://afisha.yandex.ru/moscow/theatre_show/beshenye-dengi-teatr-im-maiakovskogo"
        event.categories = {"theatre", "theatre_show", "nearest-events", "comedy", "season-premiere", "top-persons",
                            "hitprodazh-badge", "newyear-vacations", "theatre-feedback", "family-theatre",
                            "traditional-theatre", "theater"}
        event.image = "https://avatars.mds.yandex.net/get-afishanew/21422/5543036bb12f14c5b8ac13e180071c83/s270x135"
        event.start_time = start_time
        event.finish_time = finish_time
        event.join_anytime = False
        event.duplicate_id = duplicate_id
        event.status = "active"
        event.price_min = 400
        event.price_max = 6000
        return event
