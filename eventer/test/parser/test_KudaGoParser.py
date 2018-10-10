import pytest
from KudaGoParser import KudaGoParser

def test_parsing_usual_two_events():
    test_parsing_pointer = TestParsingPointer(12345678)
    session = TestSession()
    parser = KudaGoParser(session)
    parser.main(parsing_pointer=test_parsing_pointer)

def test_make_url_for_first_page():
    session = TestSession()
    parser = KudaGoParser(session)
    assert parser._make_url(1) == "https://kudago.com/public-api/v1.4/events/?lang=ru&page_size=100&order_by=-publication_date&text_format=html&location=msk&is_free=0&fields=id,publication_date,dates,title,short_title,slug,place,description,body_text,location,categories,tagline,age_restriction,price,is_free,images,favorites_count,comments_count,site_url,tags,participants&page=1"


class TestParsingPointer:

    def __init__(self, current_pointer):
        self.current_pointer = current_pointer


class TestSession:

    def __init__(self):
        self.object_in_session = []

    def add(self, obj):
        self.object_in_session.append(obj)
