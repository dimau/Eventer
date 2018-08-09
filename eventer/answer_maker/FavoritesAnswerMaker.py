from answer_maker.AbstractAnswerMaker import AbstractAnswerMaker
from Event import Event
from User import User
from Rating import Rating


class FavoritesAnswerMaker(AbstractAnswerMaker):

    def __repr__(self):
        return "<FavoritesAnswerMaker intent: {}, result_of_classification: {}>".format(self.intent, str(self.result_of_classification))

    def get_answer(self):
        # Intent will be useful for view functions
        answer = {"intent": self.intent}

        # Extract all favorites events
        all_favorites_events = self.session.query(Event).join(Rating).join(User) \
            .filter(User._id == self.user.user_id) \
            .filter(Rating._like == 1) \
            .filter(Event._start_time >= self._get_current_utc_timestamp()) \
            .order_by(Event._start_time).all()

        # Replace all latest main events by their earliest duplicates
        earliest_favorites_events = []
        for event in all_favorites_events:
            if not event.duplicate_id:
                earliest_favorites_events.append(event)
                continue
            earliest_event_in_series = self.session.query(Event)\
                .filter(Event._duplicate_id == event.duplicate_id)\
                .filter(Event._start_time >= self._get_current_utc_timestamp())\
                .order_by(Event._start_time).first()
            earliest_favorites_events.append(earliest_event_in_series)

        # Sort earliest_favorites_events
        earliest_favorites_events.sort(key=lambda event: event.start_time)

        # Prepare text answer for list
        answer["list_of_events"] = earliest_favorites_events
        if len(answer['list_of_events']) > 0:
            answer["text"] = "Вот список мероприятий, которые тебе понравились"
        else:
            answer["text"] = "Здесь будет список мероприятий, которые тебе понравились"
        answer["status"] = "list_of_events"
        return answer
