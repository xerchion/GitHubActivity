from src.Api import Api
from src.EventManager import EventManager
from src.UserInterface import UserInterface

user_interface = UserInterface()

# Get name user from args in app call
user_name = user_interface.catch_intro()

api = Api(user_name)

event_manager = None


def main():
    # Check if the request was successful
    if api.is_connection_ok():
        # Create the event manager
        event_manager = EventManager(api.extract_data())

        # Find events and their repositories
        analyzed = event_manager.analize_events()

        # Count and group identical events from the same repository
        resume_list_events = event_manager.events_counter_repo(analyzed)

        # Generate output with summaries
        output = event_manager.generate_output(resume_list_events)

        # Display the output
        user_interface.show(output, user_name)
    else:
        user_interface.message(api.get_error())


if __name__ == "__main__":
    main()
