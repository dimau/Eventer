import pytest
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from Base_class_sql_alchemy import Base


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
        assert event1._source == event2._source
        assert event1._title == event2._title
        assert event1._description == event2._description
        assert event1._id_kudago == event2._id_kudago
        assert event1._categories_kudago == event2._categories_kudago
        assert event1._tags_kudago == event2._tags_kudago
        assert event1._price_kudago == event2._price_kudago
        assert event1._url == event2._url
        assert sorted(event1._categories.split("|")) == sorted(event2._categories.split("|"))
        assert event1._image == event2._image
        assert event1._start_time == event2._start_time
        assert event1._finish_time == event2._finish_time
        assert event1._join_anytime == event2._join_anytime
        assert event1._duplicate_source_id == event2._duplicate_source_id
        assert event1._duplicate_id == event2._duplicate_id
        assert event1._price_min == event2._price_min
        assert event1._price_max == event2._price_max