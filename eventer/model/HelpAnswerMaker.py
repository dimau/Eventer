from AbstractAnswerMaker import AbstractAnswerMaker


class HelpAnswerMaker(AbstractAnswerMaker):

    def __repr__(self):
        return "<HelpAnswerMaker intent: {}, result_of_classification: {}>".format(self.intent, str(self.result_of_classification))

    def get_answer(self):
        # Intent will be useful for view functions
        answer = {"intent": self.intent}

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
