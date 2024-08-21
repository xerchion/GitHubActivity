from Api import Api
from EventManager import EventManager
from UserInterface import User_In

user_interface = User_In()

# Get name user from args in app call
user_name = user_interface.catch_intro()

api = Api(user_name)

event_manager = ""


def main():

    # Verifica que la solicitud fue exitosa
    if api.is_conection_ok():

        # Crea el gestor de eventos
        event_manager = EventManager(api.extract_data())

        # encuentra los eventos y su repo
        analized = event_manager.analize_events()

        # cuenta y agrupa los eventos iguales del mismo repo
        resume_list_events = event_manager.events_counter_repo(analized)

        # Genera la salida con comentarios
        output = event_manager.generate_output(resume_list_events)

        # visualizarlo:
        user_interface.show(output, user_name)
    else:
        user_interface.message(api.get_error())


main()
