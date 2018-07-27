import sqlalchemy
from Base_class_sql_alchemy import Base

# Параметры для конфиг файла
user_for_mysql = "eventer"
password_for_mysql = "Nhgbf86jmnIK"

engine = sqlalchemy.create_engine("mysql://" + user_for_mysql + ":" + password_for_mysql + "@localhost/eventer?charset=utf8", echo=False)

Base.metadata.create_all(engine)
