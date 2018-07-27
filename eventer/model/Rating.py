import sqlalchemy
from Base_class_sql_alchemy import Base


class Rating(Base):

    __tablename__ = 'ratings'

    _id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    _user_id = sqlalchemy.Column(sqlalchemy.Integer)
    _event_id = sqlalchemy.Column(sqlalchemy.Integer)
    _like = sqlalchemy.Column(sqlalchemy.Integer) # 0 - user doesn't like this event 1 - user likes this event 2 - user has seen this event but doesn't rate it

    def __init__(self, user_id=0, event_id=0, like=2):
        self._user_id = user_id
        self._event_id = event_id
        self._like = like

    def __repr__(self):
        return "<Rating _id: {}," \
               "_user_id: {}," \
               "_event_id: {}," \
               "_like: {}>".format(self._id,
                                   self._user_id,
                                   self._event_id,
                                   self._like)
