from AbstractAnswerMaker import AbstractAnswerMaker
from Rating import Rating
from Event import Event
import logging


class LikeDislikeAnswerMaker(AbstractAnswerMaker):

    def __repr__(self):
        return "<LikeDislikeAnswerMaker intent: {}, result_of_classification: {}>".format(self.intent, str(self.result_of_classification))

    def get_answer(self):
        # Intent will be useful for view functions
        answer = {"intent": self.intent}

        # We will work with last queue of events for this user and we will change it in database
        last_queue_events = self.user.last_queue_events
        self.session.add(self.user)
        logging.debug('Value of last_queue_events: %s', last_queue_events)

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
            if next_event.price_min:
                answer['price_min'] = next_event.price_min
            if next_event.price_max:
                answer['price_max'] = next_event.price_max
            answer["url"] = next_event.url
            answer["img"] = next_event.image
            answer["status"] = "one_event"
            self.user.delete_previous_event_from_queue()

        # Save all changes to database
        self.session.commit()
        return answer
