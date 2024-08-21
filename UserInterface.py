import sys

from constants import ACTIVITY_TEXT, ERROR_IN
from View import View


class User_In:
    def __init__(self):
        self.err = ""
        self.view = View()

    def catch_intro(self) -> str:
        unique = "único" if len(sys.argv) > 2 else ""
        if len(sys.argv) != 2:
            self.view.alert(ERROR_IN)
            exit()
        return sys.argv[1]

    def show(self, output, user):
        self.view.header(ACTIVITY_TEXT + user)
        for line in output:
            self.view.info("- " + line)

    def message(self, msg):
        self.view.alert(msg)
