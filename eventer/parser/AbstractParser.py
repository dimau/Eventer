import time
import datetime
import requests
from Event import Event


class AbstractParser:

    def __init__(self, session):
        self._session = session

    def main(self):
        """
        This method downloads list of events from source (in cycle with parameter page number)
        and save new data to database while we face parsing pointer (it means, that we have reached last successfully
        handled event from this source)
        :return:
        """
        # Define last event from previous parsing session. When we reach it, we stop parsing.
        parsing_pointer = self._create_parsing_pointer()
        self._session.add(parsing_pointer)

        # Look over all pages while we don't reach a parsing pointer
        page_number = 1
        old_event_in_collection = False
        while True:
            url = self._make_url(page=page_number)
            url_content = self._get_url_content(url)
            events_collection_source = self._list_parser(url_content)

            # Look over all events from list and create normalize dictionary for every event
            events_collection_normalized = []
            for item in events_collection_source:
                events = self._item_parser(item)

                # Save new parsing pointer - only in the beginning of this iteration of parsing
                if page_number == 1:
                    parsing_pointer.current_pointer = self._new_parsing_pointer(events[0])

                # Check parsing pointer for every event to avoid duplicates in database
                if self._check_parsing_pointer(events[0], parsing_pointer):
                    old_event_in_collection = True
                    continue
                events_collection_normalized += events

            # Remove events which have finished in past
            events_collection_normalized = self._remove_already_finished_events(events_collection_normalized)
            print("KudaGoParser:main(): page number: " + str(page_number)
                  + " new events: " + str(len(events_collection_normalized))
                  + " is existing event on the page: " + str(old_event_in_collection))

            # Save new set of events to database
            self._write_events_to_db(events_collection_normalized)

            # List of events from source has to be sorted by field where is value for parsing pointer.
            # If we have an event more than parsing pointer, it means that we work with event was
            # parsed last time and we don't have to continue
            if old_event_in_collection or page_number == 2:
                break

            page_number += 1

            # Add sleep to don't ddos attack source server
            time.sleep(1)

    def _create_parsing_pointer(self):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _make_url(self, page):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _get_url_content(self, url):
        """
        Return object Request with full HTML (or JSON dictionary for KudaGo) for url
        :param url:
        :return:
        """
        print("AbstractParser:_get_url_content(): enter")
        # TODO: make retries for request
        with requests.get(url) as req:
            return req

    def _list_parser(self, url_content):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _check_parsing_pointer(self, item, parsing_pointer):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _item_parser(self, item):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _new_parsing_pointer(self, event_dictionary):
        raise NotImplementedError("This method doesn't implemented in the concrete class")

    def _remove_already_finished_events(self, events):
        result = []
        # TODO: refactoring 3 - will have be in config file
        current_timestamp = (datetime.datetime.now() + datetime.timedelta(
            hours=3)).timestamp()  # server time is least for 3 hours than real moscow time
        for event in events:
            if event['finish_time'] > current_timestamp:
                result.append(event)
        return result

    def _write_events_to_db(self, events_collection_normalized):
        """
        Writes list with events to database
        :param events_collection_normalized:
        :return:
        """
        print("AbstractParser:_write_events_to_db(): enter")

        # Запись всех новых событий в базу данных
        for item in events_collection_normalized:
            event = Event(item)
            self._session.add(event)
        self._session.commit()

        # Assignment real id of last event for duplicates of this event with other dates
        handled_duplicate_source_id = []
        for item in events_collection_normalized:
            if item['duplicate_source_id'] == "" or item['duplicate_source_id'] in handled_duplicate_source_id:
                continue
            all_duplicates = self._session.query(Event).filter(Event._duplicate_source_id == item['duplicate_source_id']).all()
            latest_event_id = sorted(all_duplicates, key=lambda x: x.start_time, reverse=True)[0].event_id
            for event in all_duplicates:
                event.duplicate_id = latest_event_id
                self._session.add(event)
                # print(" ******************************** \n" + str(event))
            handled_duplicate_source_id.append(item['duplicate_source_id'])
        self._session.commit()
        return
