import sqlalchemy


class UserRequest:

    def __init__(self, user_message_text, result_of_classification):
        print("Внутри конструктора")
        self.user_message_text = user_message_text
        self.intent = result_of_classification['intent_name']
        self.result_of_classification = result_of_classification
        print("Внутри конца конструктора")

    def __repr__(self):
        return "UserRequest intent: {}, result_of_classification: {}".format(self.intent, str(self.result_of_classification))

    def get_answer(self):

        print("Внутри построения ответа")

        if self.intent == 'Greeting':
            return "Привет, дорогой друг! Какие мероприятия тебя интересуют?"

        if self.intent == 'Find events':
            answer = "Вы хотите узнать о " + self.result_of_classification['type-of-action'] + " которые состоятся " + self.result_of_classification['date']
            return answer

        return "Ответ заглушкой"
