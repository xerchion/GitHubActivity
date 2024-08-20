from typing import List

from Event import Event
from constants import EVENTS


class Report:
    def __init__(self, data) -> None:
        self.storage: List[Event] = []
        self.data = data
        self.extract(data)
        self.date = "Fecha y hora"

    def extract(self, data):
        for element in data:
            event = Event(element)
            self.storage.append(event)

    def prepare_view(self):
        return self.data

    def show_structure(self):
        pass

    def get_events(self, event_name):
        result = []
        for event in self.storage:
            if event.get_name() == event_name:
                result.append(event)
        return result

    def sumary(self):
        push = result = 0
        for element in self.storage:
            if element.get_name() == "CreateEvent":
                result += 1
        for element in self.storage:
            if element.get_name() == "PushEvent":
                push += 1
        return "Ha creado repositorios: " + str(push)
