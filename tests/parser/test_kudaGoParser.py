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
        event = self.create_event_kudago_exhibition_face2face()
        parser = KudaGoParser(session, mode="only_new", page_limit=1000)
        assert parser.main(test_url="http://127.0.0.1:5000?source=kudago&testcase=one_event") == 2
        event_from_db = session.query(Event).first()
        self.check_equivalence_of_two_events(event, event_from_db)

    def test_parsing_only_old_event_on_the_first_page_in_only_new_mode(self, session, clear_data):
        parsing_pointer = ParsingPointer.get_parsing_pointer(source="KudaGo", session=session)
        parsing_pointer.current_pointer = "1539356260"
        session.add(parsing_pointer)
        session.commit()
        parser = KudaGoParser(session, mode='only_new', page_limit=1000)
        assert parser.main(test_url="http://127.0.0.1:5000?source=kudago&testcase=only_old_event_on_the_first_page_in_only_new_mode") == 1
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
        parser = KudaGoParser(session, mode='full', page_limit=1000)
        assert parser.main(test_url="http://127.0.0.1:5000?source=kudago&testcase=four_pages_in_full_mode") == 4
        events_from_db = session.query(Event).all()
        assert len(events_from_db) == 2

    def test_parsing_page_with_bad_json_format_in_full_mode(self, session, clear_data):
        parser = KudaGoParser(session, mode='full', page_limit=1000)
        assert parser.main(test_url="http://127.0.0.1:5000?source=kudago&testcase=page_with_bad_json_format") == 1
        events_from_db = session.query(Event).all()
        assert len(events_from_db) == 0

    def test_parsing_page_with_404_status_code(self, session, clear_data):
        parser = KudaGoParser(session, mode='full', page_limit=1000)
        assert parser.main(test_url="http://127.0.0.1:5000?source=kudago&testcase=404") == 1
        events_from_db = session.query(Event).all()
        assert [] == events_from_db

    def test_make_url_for_second_page(self, session, clear_data):
        parser = KudaGoParser(session, mode='full', page_limit=1000)
        assert parser._make_url(page=2,
                                test_url=None) == "https://kudago.com/public-api/v1.4/events/?lang=ru&page_size=100&order_by=-publication_date&text_format=html&location=msk&is_free=0&fields=id,publication_date,dates,title,short_title,slug,place,description,body_text,location,categories,tagline,age_restriction,price,is_free,images,favorites_count,comments_count,site_url,tags,participants&page=2"

    def test_make_url_with_test_url(self, session, clear_data):
        parser = KudaGoParser(session, mode='full', page_limit=1000)
        assert parser._make_url(page=1, test_url="http://127.0.0.1:5000?source=kudago&testcase=404") == "http://127.0.0.1:5000?source=kudago&testcase=404&page=1"
