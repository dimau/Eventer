import sqlalchemy
from Model.Base_class_sql_alchemy import Base

engine = sqlalchemy.create_engine("mysql://eventer:88nJnmd446HbngYh-DDvb@localhost/eventer?charset=utf8", echo=True)

import Event
import User

Base.metadata.create_all(engine)
