from collections import Counter

from constants import COUNTER_TEXT, EVENTS_LONG_TEXT
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
            data.append({event.type: event.repo.name})
        return data

    def events_counter_repo(self, data):
        # Contar la frecuencia de cada diccionario
        dict_counter = Counter(frozenset(item.items()) for item in data)
        resume_list_events = []  # Mostrar los diccionarios que aparecen más de una vez
        for dict_key, count in dict_counter.items():
            if count > 1:
                resume_list_events.append((dict(dict_key), count))
        return resume_list_events

    def generate_output(self, data):
        texts = []
        for element in data:
            key = self.get_key(element)

            text = EVENTS_LONG_TEXT[key]

            repeat = str(element[1])
            my_dict = self.get_dict(element)
            repo = my_dict[key]
            texts.append(text + " " + str(repeat) + COUNTER_TEXT + repo)
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

    def get_events(self):
        return self.events
