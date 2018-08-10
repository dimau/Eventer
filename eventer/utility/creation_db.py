# -*- coding: utf-8 -*-

import os
import sqlalchemy
from Base_class_sql_alchemy import Base

# Start session with database
user_for_mysql = os.environ.get("USERMYSQL", None)
if not user_for_mysql:
    raise KeyError("Cannot find environment variable USERMYSQL")
password_for_mysql = os.environ.get("PASSWORDMYSQL", None)
if not password_for_mysql:
    raise KeyError("Cannot find environment variable PASSWORDMYSQL")
name_of_database_for_mysql = os.environ.get("DATABASEMYSQL", None)
if not name_of_database_for_mysql:
    raise KeyError("Cannot find environment variable DATABASEMYSQL")
engine = sqlalchemy.create_engine(
    "mysql://" + user_for_mysql + ":" + password_for_mysql + "@localhost/" + name_of_database_for_mysql + "?charset=utf8", echo=False)

import Event
import User
import Rating
import ParsingPointer

# Creation not existing tables in database
Base.metadata.create_all(engine)
