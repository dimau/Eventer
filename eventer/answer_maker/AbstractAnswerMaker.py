import datetime
from Event import Event


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

    def make_one_event_data_card(self, event):
        """
        Return dictionary with data for card about one event
        :param event:
        :return:
        """
        answer = {}
        answer["text"] = event.title.capitalize()
        answer['datetime'] = []
        if event.duplicate_id:
            for start_time, in self.session.query(Event._start_time).filter(Event._duplicate_id == event.duplicate_id):
                if start_time < self._get_current_utc_timestamp():
                    continue
                answer['datetime'].append(start_time)
                answer['datetime'].sort()
        else:
            answer['datetime'].append(event.start_time)
        if event.price_min is not None:
            answer['price_min'] = event.price_min
        if event.price_max is not None:
            answer['price_max'] = event.price_max
        answer["url"] = event.url
        answer["img"] = event.image
        answer["status"] = "one_event"
        return answer

    @staticmethod
    def _get_current_utc_timestamp():
        return int(datetime.datetime.now().timestamp())  # on our server UTC local time
