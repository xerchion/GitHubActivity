from typing import List

from constants import EVENTS
from models.github import GitHubEvent


class EventManager:
    def __init__(self, events: List[GitHubEvent]):
        self.events = events

    def get_summary(self) -> dict:
        """
        Obtiene un resumen de los eventos, como el número total de eventos
        y el número de eventos por tipo.

        :return: Diccionario con el resumen de eventos.
        """
        result = {}  # type: ignore
        for type_event in EVENTS:
            print(type_event)
            for event in self.events:
                if event.type == type_event:
                    if type_event in result.keys():
                        counter = result[type_event] + 1
                        result = {type_event: counter}

        return result

    def analyze_events(self) -> tuple:
        """
        Realiza un análisis detallado de los eventos. Esto podría incluir
        análisis más complejos como los eventos más frecuentes, patrones
        entre actores, etc.

        :return: Resultados del análisis en un formato adecuado.
        """
        # Ejemplo de análisis básico: eventos más frecuentes
        from collections import Counter

        event_types = [event.type for event in self.events]
        print(event_types)
        event_type_counts = Counter(event_types)

        return event_type_counts.most_common()

    def sumary_event(self, type, repo):
        # recibe un tipo de evento y extrae un resumen del mismo:
        # cuantas veces se repite del mismo repo
        sumary = {}
        for event in self.events:
            if type == event.type and repo == event.repo.name:
                counter = sumary[(type, repo)] + 1
                sumary[(type, repo)] = counter
        return (
            "ha hecho el evento "
            + type
            + str(sumary[(type, repo)])
            + " veces"
            + "en el repositorio: "
            + repo
        )

    def get_repos(self):
        repos = set()
        for element in self.events:
            if element.repo.name not in repos:
                repos.add(element.repo.name)
        return repos


# # Ejemplo de uso
# events = [
#     GitHubEvent(id="1", type="PushEvent", actor=..., repo=..., created_at="..."),
#     ...,
# ]
# manager = EventManager(events)

# # Añadir un nuevo evento
# new_event = GitHubEvent(
#     id="2", type="IssuesEvent", actor=..., repo=..., created_at="..."
# )
# manager.add_event(new_event)

# # Obtener un resumen
# summary = manager.get_summary()
# print(summary)

# # Analizar eventos
# analysis = manager.analyze_events()
# print(analysis)
