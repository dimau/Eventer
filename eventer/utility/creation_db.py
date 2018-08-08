# -*- coding: utf-8 -*-

import sqlalchemy
from Base_class_sql_alchemy import Base

# Parameters for config file
user_for_mysql = "eventer"
password_for_mysql = "Nhgbf86jmnIK"

engine = sqlalchemy.create_engine("mysql://" + user_for_mysql + ":" + password_for_mysql + "@localhost/eventer?charset=utf8", echo=False)

import Event
import User
import Rating
import ParsingPointer

# Creation not existing tables in database
Base.metadata.create_all(engine)
