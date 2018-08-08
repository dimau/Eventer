import datetime


class AbstractAnswerMaker:

    def __init__(self, session_with_db=None, user=None, intent="", result_of_classification=None):
        """
        Constructor for class AbstractAnswerMaker
        :param session_with_db: session sqlalchemy to work with database
        :param user: object of class User with information about user
        """

        # Initial data - session with database and user
        self.session = session_with_db
        self.user = user
        self.intent = intent
        self.result_of_classification = result_of_classification

    def get_answer(self):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    @staticmethod
    def _get_current_utc_timestamp():
        return int(datetime.datetime.now().timestamp())  # on our server UTC local time
