# -*- coding: utf-8 -*-

import os
import logging
import sqlalchemy
from sqlalchemy.orm import sessionmaker


class AbstractController:

    def _launch_logging(self, log_file_name, log_level="INFO"):
        numeric_level = getattr(logging, log_level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError("Invalid log level: {}".format(log_level))
        logging.basicConfig(format='%(levelname)s - %(asctime)s - %(module)s - %(funcName)s - %(message)s',
                            level=numeric_level,
                            filename='/var/log/eventer/' + log_file_name
                            )

    def _create_session_with_db(self):
        user_for_mysql = os.environ.get("USERMYSQL", None)
        if not user_for_mysql:
            logging.error("Cannot find environment variable USERMYSQL")
            raise KeyError("Cannot find environment variable USERMYSQL")
        password_for_mysql = os.environ.get("PASSWORDMYSQL", None)
        if not password_for_mysql:
            logging.error("Cannot find environment variable PASSWORDMYSQL")
            raise KeyError("Cannot find environment variable PASSWORDMYSQL")
        name_of_database_for_mysql = os.environ.get("DATABASEMYSQL", None)
        if not name_of_database_for_mysql:
            logging.error("Cannot find environment variable DATABASEMYSQL")
            raise KeyError("Cannot find environment variable DATABASEMYSQL")
        engine = sqlalchemy.create_engine(
            "mysql://" + user_for_mysql + ":" + password_for_mysql + "@localhost/" + name_of_database_for_mysql + "?charset=utf8",
            echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
