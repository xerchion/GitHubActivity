from collections import Counter
from typing import List

from constants import EVENTS, EVENTS_LONG_TEXT
from models.github import GitHubEvent


class EventManager:

    def __init__(self, data):
        self.events = self.data_conversion(data)

    def data_conversion(self, data):
        # Convertir la respuesta JSON en objetos Pydantic
        return [GitHubEvent(**event) for event in data]

    def analize_events(self):
        # extrae una lista con los tipos de evento y su repositorio
        data = []
        for event in self.events:
            # print(f"Event ID: {event.id}, Type: {event.type}, Repo: {event.repo.name}")
            data.append({event.type: event.repo.name})
        print(data)
        return data

    def events_counter_repo(self, data):
        # Contar la frecuencia de cada diccionario
        dict_counter = Counter(frozenset(item.items()) for item in data)
        resume_list_events = []  # Mostrar los diccionarios que aparecen más de una vez
        for dict_key, count in dict_counter.items():
            if count > 1:
                resume_list_events.append((dict(dict_key), count))
        print(resume_list_events)
        return resume_list_events

    def generate_output(self, data):
        texts = []
        for element in data:
            key = self.get_key(element)
            # print("tipo de key", dict_key)
            # print(key[0])
            text = EVENTS_LONG_TEXT[key]

            repeat = str(element[1])
            my_dict = self.get_dict(element)
            repo = my_dict[key]
            texts.append(text + " " + str(repeat) + " veces en el repositorio: " + repo)
        return texts

    # ! separarlo RECUERDA:  PRINCIPIO DE RESPONSABILIDAD UNICA
    def get_key(self, element):
        # devuelve la clave de un diccionario dentro de una tupla
        # Para extraer la key
        dicctionary = self.get_dict(element)
        # Extraer la clave del diccionario
        return list(dicctionary.keys())[0]

    def get_dict(self, element):
        # desempaqueto la tupla element
        my_dict, _ = element
        return my_dict

    # --------------------------------------------------

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
