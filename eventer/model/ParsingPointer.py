import sqlalchemy
from Base_class_sql_alchemy import Base
import logging


class ParsingPointer(Base):

    __tablename__ = 'parsing_pointers'

    _id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    _source = sqlalchemy.Column(sqlalchemy.String(150))
    _current_pointer = sqlalchemy.Column(sqlalchemy.String(150))

    def __init__(self, source=None, session=None):
        logging.debug('Enter to the method')
        self.source = source
        self.session = session

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = str(value)

    @property
    def current_pointer(self):
        return self._current_pointer

    @current_pointer.setter
    def current_pointer(self, value):
        self._current_pointer = str(value)

    @staticmethod
    def get_parsing_pointer(source, session):
        parsing_pointer = session.query(ParsingPointer) \
            .filter(ParsingPointer._source == source) \
            .first()
        if not parsing_pointer:
            parsing_pointer = ParsingPointer(source=source, session=session)
        return parsing_pointer
