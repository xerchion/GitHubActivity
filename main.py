import json
from collections import Counter

from Api import Api
from constants import EVENTS_LONG_TEXT
from EventManager import EventManager
from models.github import GitHubEvent
from User_In import User_In
from View import View

view = View()

# Get name user from args in app call
user_name = User_In.catch_intro()

api = Api(user_name)

# Verifica que la solicitud fue exitosa
if api.is_conection_ok():
    # Convierte la respuesta a JSON
    data = api.extract_data()

    # Convertir la respuesta JSON en objetos Pydantic
    events = [GitHubEvent(**event) for event in data]
    data = []
    for event in events:
        # print(f"Event ID: {event.id}, Type: {event.type}, Repo: {event.repo.name}")
        data.append({event.type: event.repo.name})
    print(data)
    # Contar la frecuencia de cada diccionario
    dict_counter = Counter(frozenset(item.items()) for item in data)
    resume_list_events = []  # Mostrar los diccionarios que aparecen más de una vez
    for dict_key, count in dict_counter.items():
        if count > 1:
            resume_list_events.append((dict(dict_key), count))
    print(resume_list_events)
    texts = []
    for element in resume_list_events:
        # Para extraer la key
        # desempaqueto la tupla element
        my_dict, number = element
        # Extraer la clave del diccionario
        key = list(my_dict.keys())[0]

        # print("tipo de key", dict_key)
        # print(key[0])
        text = EVENTS_LONG_TEXT[key]
        print
        repeat = str(element[1])
        repo = my_dict[key]
        texts.append(text + " " + str(repeat) + " veces en el repositorio: " + repo)

    # visualizarlo:
    for text in texts:
        print(text)
else:
    print(f"Error en la solicitud: {api.get_error()}")
