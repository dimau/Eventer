from answer_maker.AbstractAnswerMaker import AbstractAnswerMaker


class HelpAnswerMaker(AbstractAnswerMaker):

    def __repr__(self):
        return "<HelpAnswerMaker intent: {}, result_of_classification: {}>".format(self.intent,
                                                                                   str(self.result_of_classification))

    def get_answer(self):
        # Intent will be useful for view functions
        answer = {"intent": self.intent}

        # Special beginning for new user
        if self.intent == "Start":
            answer["text"] = "Привет! "
        else:
            answer["text"] = ""
        answer["text"] += "Я подскажу, куда сходить в Москве :)\n\n" \
                          "Можешь общаться со мной обычными фразами, указывая категорию событий и даты, которые тебе интересны:\n\n" \
                          "- Куда сходить сегодня вечером\n" \
                          "- Куда сходить в театр на выходных\n" \
                          "- Кино завтра\n" \
                          "- Спектакли в пятницу\n" \
                          "- Куда пойти с ребенком на следующей неделе\n\n" \
                          "Если событие тебе интересно, нажми 'Запомнить', все понравившиеся события будут доступны по кнопке 'Избранное'.\n\n" \
                          "Если событие тебе НЕинтересно, нажми 'Следующее', оно больше не будет показываться.\n\n" \
                          "Эту инструкцию и список основных категорий всегда можно посмотреть по кнопке 'Помощь'"
        answer['message_buttons'] = ['Концерты', 'Театр', 'Образование', 'Вечеринки',
                                     'Спорт', 'Выставки', 'Экскурсии', 'Фестивали', 'Кино', 'Игры',
                                     'Знакомства', 'Танцы', 'Для детей', 'Стендап']
        answer["status"] = "none_event"
        return answer
