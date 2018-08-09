from answer_maker.AbstractAnswerMaker import AbstractAnswerMaker


class GreetingAnswerMaker(AbstractAnswerMaker):

    def __repr__(self):
        return "<GreetingAnswerMaker intent: {}, result_of_classification: {}>".format(self.intent, str(self.result_of_classification))

    def get_answer(self):
        # Intent will be useful for view functions
        answer = {"intent": self.intent}

        answer["text"] = "Привет, дорогой друг! Какие мероприятия тебя интересуют?"
        answer["status"] = "none_event"
        return answer
