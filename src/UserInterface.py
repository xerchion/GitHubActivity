import sys

from .constants import ACTIVITY_SUMMARY_TEXT, INVALID_PARAMETERS_MESSAGE
from .View import View


class UserInterface:
    def __init__(self):
        self.err = ""
        self.view = View()

    def catch_intro(self) -> str:
        # Returns the command-line argument if exactly one is provided.

        if len(sys.argv) != 2:
            self.view.alert(INVALID_PARAMETERS_MESSAGE)
            exit()
        return sys.argv[1]

    def show(self, output, user):
        # Displays the header and each line of the output.
        self.view.header(ACTIVITY_SUMMARY_TEXT + user)
        for line in output:
            self.view.info("- " + line)

    def message(self, msg):
        self.view.alert(msg)
