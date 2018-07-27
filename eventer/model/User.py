import sqlalchemy
from Base_class_sql_alchemy import Base


class User(Base):
    __tablename__ = 'users'

    _id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    _telegram_id = sqlalchemy.Column(sqlalchemy.Integer)
    _name = sqlalchemy.Column(sqlalchemy.String(50))
    _last_queue_events_str = sqlalchemy.Column(sqlalchemy.String(2000))  # Here we save sorted by relevance list of events from last request in string format

    def __init__(self, telegram_id=None, name=""):
        self._telegram_id = telegram_id
        self._name = name
        self._last_queue_events_str = ""

    def __repr__(self):
        return "<User _id: {}, " \
               "_telegram_id: {}, " \
               "_name: {}," \
               "_last_queue_events_str: {}>".format(self._id,
                                                    self._telegram_id,
                                                    self._name,
                                                    self._last_queue_events_str[0:20])

    @property
    def user_id(self):
        return self._id

    @property
    def last_queue_events(self):
        # Empty string = empty list
        if self._last_queue_events_str == "":
            return []
        # Split string to list and conversion to integer
        # It is important to save the order of elements
        array = self._last_queue_events_str.split("|")
        for i in range(len(array)):
            print(i)
            array[i] = int(array[i])
        # TODO: test
        print("геттер отработал, значение: " + str(array))
        return array

    @last_queue_events.setter
    def last_queue_events(self, queue):
        """
        Setter for property last_queue_events (synonym for _last_queue_events_str), but for external people it works
        as a list, not a string.
        :param queue: We are waiting for a list of integers here (event id-s)
        :return:
        """
        # Special work for empty lists
        if len(queue) == 0:
            self._last_queue_events_str = ""
            return
        # Construction string from list, we have to convert values from integer to string
        final_string = ""
        for item in queue:
            final_string += str(item) + "|"
        final_string = final_string[:-1]  # Remove last symbol "|"
        self._last_queue_events_str = final_string
        # TODO: test
        print("сеттер отработал, значение: " + self._last_queue_events_str)

    def delete_previous_event_from_queue(self):
        list_of_events = self.last_queue_events
        del list_of_events[0]
        self.last_queue_events = list_of_events

    def clear_last_queue_events(self):
        self._last_queue_events_str = ""
