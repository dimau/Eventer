from answer_maker.AbstractAnswerMaker import AbstractAnswerMaker


class FallbackAnswerMaker(AbstractAnswerMaker):

    def __repr__(self):
        return "<FallbackAnswerMaker intent: {}, result_of_classification: {}>".format(self.intent, str(self.result_of_classification))

    def get_answer(self):
        # Intent will be useful for view functions
        answer = {"intent": self.intent}

        answer["text"] = "Что-то я вас не понял, так какие события вас интересуют и когда?"
        answer["status"] = "none_event"
        return answer
