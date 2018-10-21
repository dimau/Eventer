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
        assert event1.source == event2.source
        assert event1.title == event2.title
        assert event1.description == event2.description
        assert event1.id_kudago == event2.id_kudago
        assert event1.categories_kudago == event2.categories_kudago
        assert event1.tags_kudago == event2.tags_kudago
        assert event1.price_kudago == event2.price_kudago
        assert event1.url == event2.url
        assert sorted(event1.categories.split("|")) == sorted(event2.categories.split("|"))
        assert event1.image == event2.image
        assert event1.start_time == event2.start_time
        assert event1.finish_time == event2.finish_time
        assert event1.join_anytime == event2.join_anytime
        assert event1.duplicate_source_id == event2.duplicate_source_id
        assert event1.duplicate_id == event2.duplicate_id
        assert event1.price_min == event2.price_min
        assert event1.price_max == event2.price_max
