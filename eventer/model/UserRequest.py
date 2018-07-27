
import apiai
import json
from Event import Event


class UserRequest:


    def __init__(self, user_message_text, session_with_db):

        # Исходные данные - текстовое сообщение, объект сессии с БД и токен для доступа к dialogflow
        self.user_message_text = user_message_text
        self.api_ai_token = "9f442ba7276d40d1aa64a32a156af507"
        self.session = session_with_db

        # Получим результаты обработки NLP
        result_of_classification = self.get_classification_and_entities()
        self.intent = result_of_classification['intent_name']
        self.result_of_classification = result_of_classification


    def __repr__(self):
        return "UserRequest intent: {}, result_of_classification: {}".format(self.intent, str(self.result_of_classification))

    def get_answer(self):
        answer = {}

        if self.intent == 'Greeting':
            answer["text"] = "Привет, дорогой друг! Какие мероприятия тебя интересуют?"
            return answer

        if self.intent == 'Find events':
            target_categories = self.get_categories_for_type_of_action(self.result_of_classification['type-of-action'])
            target_date = self.result_of_classification['date']
            relevant_event = self.get_events_for_conditions(target_date, target_categories)
            print(str(self.result_of_classification))
            if not relevant_event:
                answer["text"] = "Я не нашел событий под ваши условия, может быть переформулируете?"
                return answer
            answer["text"] = relevant_event.title.capitalize()
            answer["url"] = relevant_event.url
            answer["img"] = relevant_event.image
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
        relevant_events = set()
        try:
            for category in categories:
                relevant_events.update(self.session.query(Event).filter(Event._categories.like("%" + category + "%")).all())
        except Exception as e:
            print(str(e))

        if len(relevant_events) == 0:
            return None

        return relevant_events.pop()
