from AbstractAnswerMaker import AbstractAnswerMaker
from Event import Event
from Rating import Rating
import datetime
import logging


class FindEventsAnswerMaker(AbstractAnswerMaker):

    def __repr__(self):
        return "<FindEventsAnswerMaker intent: {}, result_of_classification: {}>".format(self.intent, str(self.result_of_classification))

    def get_answer(self):
        # Intent will be useful for view functions
        answer = {"intent": self.intent}

        target_categories = self._get_categories_for_type_of_action(self.result_of_classification['type-of-action'])
        logging.info("Target categories: %s", target_categories)
        start_timestamp, finish_timestamp = self._get_required_time_period()
        logging.info("Required time period: %s - %s or %s - %s", start_timestamp, finish_timestamp,
                     datetime.datetime.fromtimestamp(start_timestamp),
                     datetime.datetime.fromtimestamp(finish_timestamp))
        relevant_events = self._get_sorted_events_for_conditions(start_timestamp, finish_timestamp, target_categories)
        logging.debug('Sorted list of relevant events: %s', relevant_events)
        logging.info('Size of sorted list of relevant events: %s', len(relevant_events))
        if not relevant_events:
            answer["text"] = "Я не нашел новых событий под эти условия, давайте поищем что-нибудь еще?"
            answer["status"] = "none_event"
            self.user.clear_last_queue_events()
            return answer

        answer["text"] = relevant_events[0].title.capitalize()
        answer['datetime'] = relevant_events[0].start_time
        if relevant_events[0].price_min:
            answer['price_min'] = relevant_events[0].price_min
        if relevant_events[0].price_max:
            answer['price_max'] = relevant_events[0].price_max
        answer["url"] = relevant_events[0].url
        answer["img"] = relevant_events[0].image
        answer["status"] = "one_event"

        # We have to save the sorted list of relevant events for user
        self.user.last_queue_events = self._get_id_for_events_in_iterator(relevant_events)
        self.session.add(self.user)
        self.session.commit()
        return answer

    @staticmethod
    def _get_categories_for_type_of_action(type_of_action):
        """
        Список возможных типов действий, которые мы можем распознать во фразе пользователя задается в dialogflow
        Этот список может отличаться от набора тегов, присваиваемых событиям в базе данных, так как
        под одно понятие пользователя могут подходить несколько тегов в базе данных, например:
        night = night и party, comedy-club = comedy-club и stand-up и так далее.
        При этом во фразе пользователя по 1 слове мы можем выделить только какую-то одну категорию,
        отсюда и отношение: один во фразе пользовател ко многим в базе данных.
        :param type_of_action:
        :return:
        """

        if type_of_action == "":
            return set()

        type_of_action_dictionary = {
            "concert": ["concert"],
            "theater": ["theater"],
            "education": ["education"],
            "party": ["party"],
            "sport": ["sport"],
            "exhibition": ["exhibition", "permanent-exhibitions"],
            "tour": ["tour"],
            "festival": ["festival"],
            "cinema": ["cinema"],
            "fashion": ["fashion"],
            "show": ["show"],
            "social-activity": ["social-activity"],
            "games": ["games"],
            "night": ["night"],
            "meeting": ["meeting"],
            "speed-dating": ["speed-dating"],
            "flashmob": ["flashmob"],
            "masquerade": ["masquerade", "festival"],
            "romance": ["romance"],
            "dance-trainings": ["dance-trainings"],
            "evening": ["evening"],
            "discount": ["discount"],
            "stock": ["stock"],
            "sale": ["sale"],
            "shopping": ["shopping"],
            "quest": ["quest"],
            "yoga": ["yoga"],
            "presentation": ["presentation"],
            "magic": ["magic"],
            "kvn": ["kvn"],
            "comedy-club": ["comedy-club"],
            "stand-up": ["stand-up"],
            "kids": ["kids"],
            "circus": ["circus"],
            "open": ["open"],
            "other": ["other"],
            "photo": ["photo"],
            "global": ["global"],
            "business-events": ["business-events"]
        }
        return set(type_of_action_dictionary.get(type_of_action, []))

    def _get_required_time_period(self):
        # Manage with dates
        if self.result_of_classification['date_period']:
            dates = self.result_of_classification['date_period'].split("/")
            start_date = datetime.datetime.strptime(dates[0], "%Y-%m-%d")  # '2018-07-28/2018-07-29'
            finish_date = datetime.datetime.strptime(dates[1], "%Y-%m-%d")  # '2018-07-28/2018-07-29'
        elif self.result_of_classification['date']:
            start_date = datetime.datetime.strptime(self.result_of_classification['date'], "%Y-%m-%d")  # '2018-07-28'
            finish_date = start_date
        elif self.result_of_classification['time_period']:
            start_date = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)  # begin of current date
            finish_date = start_date
        else:
            start_date = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month,datetime.datetime.now().day)  # begin of current date
            finish_date = start_date + datetime.timedelta(weeks=4)

        # Manage with time
        if self.result_of_classification['date_period']:
            start_timestamp = start_date.timestamp()
            finish_timestamp = (finish_date + datetime.timedelta(hours=23, minutes=59)).timestamp()
        elif self.result_of_classification['time_period']:
            times = self.result_of_classification['time_period'].split("/")  # '16:00:00/23:59:00'
            start_times = times[0].split(":")  # '16:00:00'
            finish_times = times[1].split(":")  # '23:59:00'
            start_time_delta = datetime.timedelta(hours=int(start_times[0]), minutes=int(start_times[1]), seconds=int(start_times[2]))
            finish_time_delta = datetime.timedelta(hours=int(finish_times[0]), minutes=int(finish_times[1]), seconds=int(finish_times[2]))
            start_timestamp = (start_date + start_time_delta).timestamp()
            finish_timestamp = (finish_date + finish_time_delta).timestamp()
        else:
            start_timestamp = start_date.timestamp()
            finish_timestamp = (finish_date + datetime.timedelta(hours=23, minutes=59)).timestamp()

        # Correction for current time
        start_timestamp, finish_timestamp = self._time_correction_for_current_time(start_timestamp=start_timestamp,
                                                                                   finish_timestamp=finish_timestamp)

        # Correction for local time
        start_timestamp, finish_timestamp = self._time_correction_for_local_time(start_timestamp=start_timestamp,
                                                                                 finish_timestamp=finish_timestamp)
        return int(start_timestamp), int(finish_timestamp)

    @staticmethod
    def _time_correction_for_current_time(start_timestamp=0.0, finish_timestamp=0.0):
        """
        Start time has to be more than current server time.
        If finish time least than current time, than we will take next 24 hours.
        :param start_timestamp:
        :param finish_timestamp:
        :return:
        """
        # TODO: refactoring 3 - will have be in config file
        if start_timestamp < (datetime.datetime.now() + datetime.timedelta(
                hours=3)).timestamp():  # server time is least for 3 hours than real moscow time
            start_timestamp = (datetime.datetime.now() + datetime.timedelta(hours=3)).timestamp()
        if finish_timestamp < (datetime.datetime.now() + datetime.timedelta(hours=3)).timestamp():
            finish_timestamp = (datetime.datetime.now() + datetime.timedelta(hours=23, minutes=59)).timestamp()
        return start_timestamp, finish_timestamp

    @staticmethod
    def _time_correction_for_local_time(start_timestamp=0.0, finish_timestamp=0.0):
        """
        User tell us time as his local time, but events id database are saved with UTC timestamp
        this method convert required user local time to UTC time for work with database
        :param start_timestamp:
        :param finish_timestamp:
        :return:
        """
        return start_timestamp - 3600 * 3, finish_timestamp - 3600 * 3  # only for Moscow timezone

    def _get_events_for_conditions(self, start_timestamp, finish_timestamp, categories):
        """
        Return set of events that is fitting for user request by category, date and other conditions (NOT SORTED BY RELEVANCE)!!!
        :param start_timestamp:
        :param finish_timestamp:
        :param categories:
        :return: set of Events
        """
        relevant_events = set()
        if len(categories) != 0:  # if user writes something about categories
            for category in categories:
                relevant_events.update(self.session.query(Event).filter(
                    Event._categories.like("%" + category + "%"),
                    Event._start_time >= start_timestamp,
                    Event._start_time <= finish_timestamp
                ).all())
        else:  # if user doesn't write something about categories
            relevant_events.update(self.session.query(Event).filter(
                Event._start_time >= start_timestamp,
                Event._start_time <= finish_timestamp
            ).all())
        logging.info("Size of set of relevant events: %s", len(relevant_events))
        relevant_events = self._remove_evaluated_events(relevant_events)
        return relevant_events

    def _remove_evaluated_events(self, relevant_events):
        ids_evaluated_events = set()
        for event_id, in self.session.query(Rating._event_id).filter(Rating._user_id == self.user.user_id):
            ids_evaluated_events.add(event_id)
        result_set_of_events = set()
        removed_events = []
        for event in relevant_events:
            if event.event_id in ids_evaluated_events:
                removed_events.append(event.event_id)
                continue
            result_set_of_events.add(event)
        logging.info('Removed events: %s', removed_events)
        return result_set_of_events

    def _get_sorted_events_for_conditions(self, start_timestamp, finish_timestamp, categories):
        """
        Return sorted list of relevant events that is fitting for user request
        MAXIMUM 100 events per time
        :param start_timestamp:
        :param finish_timestamp:
        :param categories:
        :return: sorted list of Events
        """
        relevant_events = self._get_events_for_conditions(start_timestamp, finish_timestamp, categories)
        return list(relevant_events)[0:100]  # we will return for one time only 100 most relevant events

    @staticmethod
    def _get_id_for_events_in_iterator(iterator):
        list_of_id = []
        for item in iterator:
            list_of_id.append(item.event_id)
        return list_of_id
