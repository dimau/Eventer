import apiai
import json
from Event import Event
from User import User
from Rating import Rating


class UserRequest:


    def __init__(self, user_message_text="", session_with_db=None, user=None):

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
        print("Интент: " + str(self.intent) + " Сообщение: " + self.user_message_text)

        if self.intent == 'Greeting':
            answer["text"] = "Привет, дорогой друг! Какие мероприятия тебя интересуют?"
            return answer

        if self.intent == 'Find events':
            target_categories = self.get_categories_for_type_of_action(self.result_of_classification['type-of-action'])
            target_date = self.result_of_classification['date']
            # TODO: test
            print(str(self.result_of_classification))
            relevant_events = self.get_sorted_events_for_conditions(target_date, target_categories)
            if not relevant_events:
                answer["text"] = "Я не нашел событий под эти условия, давайте переформулируем?"
                answer["status"] = "none_event"
                self.user.clear_last_queue_events()
                return answer

            answer["text"] = relevant_events[0].title.capitalize()
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
                answer["url"] = next_event.url
                answer["img"] = next_event.image
                answer["status"] = "one_event"
                self.user.delete_previous_event_from_queue()

            # Save all changes to database
            self.session.commit()
            return answer

        answer["text"] = "Шестеренки за болты забежали, попробуйте еще раз"
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
            "holiday": ["holiday"],
            "social-activity": ["social-activity"],
            "yarmarki-razvlecheniya-yarmarki": ["yarmarki-razvlecheniya-yarmarki"],
            "games": ["games"],
            "night": ["night"],
            "meeting": ["meeting"],
            "speed-dating": ["speed-dating"],
            "flashmob": ["flashmob"],
            "masquerade": ["masquerade"],
            "romance": ["romance"],
            "dance-trainings": ["dance-trainings"],
            "evening": ["evening"],
            "discount": ["discount"],
            "stock": ["stock"],
            "sale": ["sale"],
            "shopping": ["shopping"],
            "quest": ["quest"],
            "ball": ["ball"],
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


    def get_events_for_conditions(self, date, categories):
        """
        Return set of events that is fitting for user request by category, date and other conditions (NOT SORTED BY RELEVANCE)!!!
        :param date:
        :param categories:
        :return: set of Events
        """
        relevant_events = set()
        try:
            for category in categories:
                relevant_events.update(self.session.query(Event).filter(Event._categories.like("%" + category + "%")).all())
        except Exception as e:
            print(str(e))

        return relevant_events

    def get_sorted_events_for_conditions(self, date, categories):
        """
        Return sorted list of relevant events that is fitting for user request
        :param date:
        :param categories:
        :return: sorted list of Events
        """
        relevant_events = self.get_events_for_conditions(date,categories)
        return list(relevant_events)

    @staticmethod
    def get_id_for_events_in_iterator(iterator):
        list_of_id = []
        for item in iterator:
            list_of_id.append(item.event_id)
        return list_of_id
