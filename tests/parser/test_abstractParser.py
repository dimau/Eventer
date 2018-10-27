from AbstractTestClass import AbstractTestClass
from KudaGoParser import KudaGoParser
from Event import Event
from User import User
from Rating import Rating
from ParsingPointer import ParsingPointer
import copy


class TestAbstractParser(AbstractTestClass):

    def test_update_events_from_db(self, session, clear_data):
        # TODO: create events in abstract test class (remember that these events emulate events from database not from url)
        # Form event № 1
        event_from_database_for_updating = Event()
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
        # Form event № 2
        event_from_source_for_updating = Event()
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
        # Form event № 3
        event_from_database_for_inactivating = Event()
        event_from_database_for_inactivating._id = 80
        event_from_database_for_inactivating.source = "KudaGo"
        event_from_database_for_inactivating.url = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event_from_database_for_inactivating.start_time = 4695469500
        event_from_database_for_inactivating.finish_time = 4699825500
        event_from_database_for_inactivating.duplicate_source_id = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event_from_database_for_inactivating.duplicate_id = 45
        event_from_database_for_inactivating.status = "active"
        # Form event № 4
        event_from_source_for_adding = Event()
        event_from_source_for_adding.source = "KudaGo"
        event_from_source_for_adding.url = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event_from_source_for_adding.start_time = 4695469900
        event_from_source_for_adding.finish_time = 4699825900
        event_from_source_for_adding.duplicate_source_id = "https://kudago.com/msk/event/vyistavka-face-2-face"
        event_from_source_for_adding.duplicate_id = 0
        event_from_source_for_adding.status = "active"
        # Form lists for events as arguments for function under testing
        events = [copy.deepcopy(event_from_source_for_updating), copy.deepcopy(event_from_source_for_adding)]
        same_events_in_db = [copy.deepcopy(event_from_database_for_updating), copy.deepcopy(event_from_database_for_inactivating)]
        # Test our function
        result_list_of_events = KudaGoParser._update_events_from_db(same_events_in_db, events)
        self.check_equivalence_of_two_events(result_list_of_events[0], event_from_source_for_updating)
        self.check_equivalence_of_two_events(result_list_of_events[1], event_from_source_for_adding)
        event_from_database_for_inactivating.status = "hidden"
        self.check_equivalence_of_two_events(result_list_of_events[2], event_from_database_for_inactivating)
        assert len(result_list_of_events) == 3
