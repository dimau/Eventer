import apiai
import json
import datetime
from Event import Event
from User import User
from Rating import Rating


class UserRequest:


    def __init__(self, user_message_text="", session_with_db=None, user=None, type="text_message"):
        """
        Constructor for class
        :param user_message_text:
        :param session_with_db:
        :param user:
        :param type: start = пользователь добавил бота; text_message - обычное текстовое сообщение
        """

        # Исходные данные - текстовое сообщение, объект сессии с БД и токен для доступа к dialogflow
        self.user_message_text = user_message_text
        self.api_ai_token = "9f442ba7276d40d1aa64a32a156af507"
        self.session = session_with_db
        self.user = user

        # Получим результаты обработки NLP
        result_of_classification = self.get_classification_and_entities()
        self.intent = result_of_classification['intent_name']
        self.result_of_classification = result_of_classification


    def __repr__(self):
        return "<UserRequest intent: {}, result_of_classification: {}>".format(self.intent, str(self.result_of_classification))

    def get_answer(self):

        # Initialize response object and immediately write there intent of the request
        # Intent will be useful for view functions
        answer = {"intent": self.intent}

        # TODO: test
        print("UserRequest:get_answer(): enter, intent: " + str(self.intent) + " message: " + self.user_message_text)

        if self.intent == 'Greeting':
            answer["text"] = "Привет, дорогой друг! Какие мероприятия тебя интересуют?"
            answer["status"] = "none_event"
            return answer

        if self.intent == 'Find events':
            target_categories = self.get_categories_for_type_of_action(self.result_of_classification['type-of-action'])
            start_timestamp, finish_timestamp = self.get_required_time_period()
            # TODO: test
            print("UserRequest:get_answer(): intent = Find events, result of classification: " + str(self.result_of_classification))
            relevant_events = self.get_sorted_events_for_conditions(start_timestamp, finish_timestamp, target_categories)
            if not relevant_events:
                answer["text"] = "Я не нашел событий под эти условия, давайте переформулируем?"
                answer["status"] = "none_event"
                self.user.clear_last_queue_events()
                return answer

            answer["text"] = relevant_events[0].title.capitalize()
            answer['datetime'] = relevant_events[0].start_time
            answer["url"] = relevant_events[0].url
            answer["img"] = relevant_events[0].image
            answer["status"] = "one_event"

            # We have to save the sorted list of relevant events for user
            self.user.last_queue_events = self.get_id_for_events_in_iterator(relevant_events)
            self.session.add(self.user)
            self.session.commit()
            return answer

        if self.intent == "Like" or self.intent == "Dislike":

            # We will work with last queue of events for this user and we will change it in database
            last_queue_events = self.user.last_queue_events
            self.session.add(self.user)
            print("в очереди вот: " + str(last_queue_events))

            # Add like or dislike for previous event
            previous_event_id = last_queue_events[0]
            value_of_like = 1 if self.intent == "Like" else 0
            rating = Rating(user_id=self.user.user_id, event_id=previous_event_id, like=value_of_like)
            self.session.add(rating)

            # In queue there isn't other events
            if len(last_queue_events) == 1:
                answer["text"] = "Больше не осталось подходящих событий, поищем что-то еще?"
                answer["status"] = "none_event"
                self.user.clear_last_queue_events()
            else:
                next_event_id = last_queue_events[1]
                next_event = self.session.query(Event).filter(Event._id == next_event_id).first()
                answer["text"] = next_event.title.capitalize()
                answer['datetime'] = next_event.start_time
                answer["url"] = next_event.url
                answer["img"] = next_event.image
                answer["status"] = "one_event"
                self.user.delete_previous_event_from_queue()

            # Save all changes to database
            self.session.commit()
            return answer

        if self.intent == 'Favorites':
            # Code snippet for test, it can show ratings with like and their events ids
            # all_liked_ratings = self.session.query(Rating).join(User).filter(User._id == self.user.user_id).filter(Rating._like == 1).all()
            # print(str(all_liked_ratings))
            all_favorites_events = self.session.query(Event).join(Rating).join(User)\
                .filter(User._id == self.user.user_id)\
                .filter(Rating._like == 1)\
                .filter(Event._start_time >= self._get_current_utc_timestamp())\
                .order_by(Event._start_time).all()
            answer["list_of_events"] = all_favorites_events
            if len(answer['list_of_events']) > 0:
                answer["text"] = "Вот список мероприятий, которые тебе понравились"
            else:
                answer["text"] = "Здесь будет список мероприятий, которые тебе понравились"
            answer["status"] = "list_of_events"
            return answer

        if self.intent == 'Help':
            # Check sign (black) = \u2713
            answer["text"] = "Я могу подсказать, куда сходить в Москве :)\n" \
                             "Скажи, какая категория событий тебе интересна и на какую дату?\n\n" \
                             "Я знаю про вот такие категории:\n" \
                             "\U0001F4CC Концерты\n" \
                             "\U0001F4CC Театр\n" \
                             "\U0001F4CC Образовательные мероприятия\n" \
                             "\U0001F4CC Вечеринки\n" \
                             "\U0001F4CC Спортивные мероприятия\n" \
                             "\U0001F4CC Выставки\n" \
                             "\U0001F4CC Экскурсии\n" \
                             "\U0001F4CC Фестивали\n" \
                             "\U0001F4CC Кино\n" \
                             "\U0001F4CC Игры\n" \
                             "\U0001F4CC Быстрые свидания\n" \
                             "\U0001F4CC Занятия танцами\n" \
                             "\U0001F4CC Детские мероприятия\n" \
                             "\U0001F4CC Стендап шоу"
            answer["status"] = "none_event"
            return answer

        answer["text"] = "Что-то я вас не понял, так какие события вас интересуют и когда?"
        answer["status"] = "none_event"
        return answer


    def get_classification_and_entities(self):
        """
        Функция возвращает результата классификации реплики пользователя и выделенные сущности
        :return: словарь с тематикой обращения и выделенными сущностями
        """
        result = {}
        request_to_apiai = apiai.ApiAI(self.api_ai_token).text_request()  # Токен API к Dialogflow
        request_to_apiai.lang = 'ru'  # На каком языке будет послан запрос
        request_to_apiai.session_id = "idSessionOfDialog"  # ID Сессии диалога (нужно, чтобы потом учить бота)
        request_to_apiai.query = self.user_message_text  # Готовим к передаче в apiai текст сообщения пользователя

        # Непосредственно выполняем запрос к apiai
        try:
            response_json_from_apiai = json.loads(request_to_apiai.getresponse().read().decode('utf-8'))
        except Exception as e:
            print("ошибка ", str(e))
            return {}

        # Получаем результат классификации сообщения пользователя
        result['intent_name'] = response_json_from_apiai['result']['metadata']['intentName']

        # Параметры для интента поиска мероприятий
        if result['intent_name'] == 'Find events':
            result['date_period'] = response_json_from_apiai['result']['parameters']['date-period']
            result['with_who'] = response_json_from_apiai['result']['parameters']['With-who']
            result['date'] = response_json_from_apiai['result']['parameters']['date']
            result['free_or_not'] = response_json_from_apiai['result']['parameters']['Free-or-not']
            result['time_period'] = response_json_from_apiai['result']['parameters']['time-period']
            result['type-of-action'] = response_json_from_apiai['result']['parameters']['Type-of-action']

        return result


    @staticmethod
    def get_categories_for_type_of_action(type_of_action):
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

    def get_required_time_period(self):
        print("UserRequest:get_required_time_period(): enter")

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

        print("UserRequest:get_required_time_period(): start_timestamp: " + str(start_timestamp) + " finish_timestamp: " + str(finish_timestamp))
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
        if start_timestamp < (datetime.datetime.now() + datetime.timedelta(hours=3)).timestamp(): # server time is least for 3 hours than real moscow time
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

    def get_events_for_conditions(self, start_timestamp, finish_timestamp, categories):
        """
        Return set of events that is fitting for user request by category, date and other conditions (NOT SORTED BY RELEVANCE)!!!
        :param start_timestamp:
        :param finish_timestamp:
        :param categories:
        :return: set of Events
        """
        print("UserRequest:get_events_for_conditions(): enter")
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
        print("UserRequest:get_events_for_conditions(): relevant_events: " + str(relevant_events)[0:20])
        return relevant_events

    def get_sorted_events_for_conditions(self, start_timestamp, finish_timestamp, categories):
        """
        Return sorted list of relevant events that is fitting for user request
        MAXIMUM 100 events per time
        :param start_timestamp:
        :param finish_timestamp:
        :param categories:
        :return: sorted list of Events
        """
        print("UserRequest:get_sorted_events_for_conditions(): enter")
        relevant_events = self.get_events_for_conditions(start_timestamp, finish_timestamp, categories)
        print("UserRequest:get_sorted_events_for_conditions(): relevant_events: " + str(list(relevant_events))[0:20])
        return list(relevant_events)[0:100]  # we will return for one time only 100 most relevant events

    @staticmethod
    def get_id_for_events_in_iterator(iterator):
        list_of_id = []
        for item in iterator:
            list_of_id.append(item.event_id)
        return list_of_id

    @staticmethod
    def _get_current_utc_timestamp():
        return int(datetime.datetime.now().timestamp())  # on our server UTC local time
