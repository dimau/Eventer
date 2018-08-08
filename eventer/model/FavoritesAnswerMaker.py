from AbstractAnswerMaker import AbstractAnswerMaker
from Event import Event
from User import User
from Rating import Rating


class FavoritesAnswerMaker(AbstractAnswerMaker):

    def __repr__(self):
        return "<FavoritesAnswerMaker intent: {}, result_of_classification: {}>".format(self.intent, str(self.result_of_classification))

    def get_answer(self):
        # Intent will be useful for view functions
        answer = {"intent": self.intent}

        all_favorites_events = self.session.query(Event).join(Rating).join(User) \
            .filter(User._id == self.user.user_id) \
            .filter(Rating._like == 1) \
            .filter(Event._start_time >= self._get_current_utc_timestamp()) \
            .order_by(Event._start_time).all()
        answer["list_of_events"] = all_favorites_events
        if len(answer['list_of_events']) > 0:
            answer["text"] = "Вот список мероприятий, которые тебе понравились"
        else:
            answer["text"] = "Здесь будет список мероприятий, которые тебе понравились"
        answer["status"] = "list_of_events"
        return answer
