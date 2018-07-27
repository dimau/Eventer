import sqlalchemy
from Base_class_sql_alchemy import Base


class User(Base):
    __tablename__ = 'users'
    _id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    _name = sqlalchemy.Column(sqlalchemy.String(50))
