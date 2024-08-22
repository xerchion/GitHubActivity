from collections import Counter
from typing import Dict, List, Tuple

from models.github import GitHubEvent

from .constants import (
    EVENTS_LONG_TEXT,
    NO_RECENT_ACTIVITY_MESSAGE,
    REPOSITORY_COUNT_TEXT,
)


class EventManager:

    def __init__(self, data: List[Dict[str, str]]):
        # Initialize EventManager with data converted into GitHubEvent objects.
        self.events = self.data_conversion(data)

    def data_conversion(self, data: List[dict]) -> List[GitHubEvent]:
        # Convert JSON response into Pydantic objects.
        return [GitHubEvent(**event) for event in data]

    def analize_events(self) -> List[Dict[str, str]]:
        # Extracts a list of dictionaries with event types and their repository names.
        return [{event.type: event.repo.name} for event in self.events]

    def events_counter_repo(
        self, data: List[Dict[str, str]]
    ) -> List[Tuple[Dict[str, str], int]]:
        # Count the frequency of each type event and same repo.
        dict_counter = Counter(frozenset(item.items()) for item in data)
        return [
            (dict(dict_key), count)
            for dict_key, count in dict_counter.items()
            if count > 1
        ]

    def generate_output(self, data: List[Tuple[Dict[str, str], int]]) -> List[str]:
        # Generate output strings from data or return a default message if no data is present.
        output = []
        for element in data:
            type_event_name = self.get_key(element)
            long_text = EVENTS_LONG_TEXT[type_event_name]
            times = str(element[1])
            repo = element[0][type_event_name]
            output.append(f"{long_text} {times}{REPOSITORY_COUNT_TEXT}{repo}")
        if not output:
            output.append(NO_RECENT_ACTIVITY_MESSAGE)
        return output

    def get_key(self, element: Tuple[Dict[str, str], int]) -> str:
        # Return the first key from a dictionary inside a tuple.
        return next(iter(element[0]))

    def get_events(self) -> List[GitHubEvent]:
        # Return the list of GitHubEvent objects.
        return self.events
