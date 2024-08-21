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

    # Crea el gestor de eventos
    event_manager = EventManager(api.extract_data())

    # encuentra los eventos y su repo
    analized = event_manager.analize_events()

    # cuenta y agrupa los eventos iguales del mismo repo
    resume_list_events = event_manager.events_counter_repo(analized)

    output = event_manager.generate_output(resume_list_events)
    # visualizarlo:
    for line in output:
        print(line)
else:
    print(f"Error en la solicitud: {api.get_error()}")
