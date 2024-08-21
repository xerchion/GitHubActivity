import sys

from View import View


class User_In:
    def __init__(self):
        pass

    @classmethod
    def catch_intro(cls) -> str:
        if len(sys.argv) != 2:
            view = View()
            view.alert("Parámetros no válidos. Se espera un único parámetro.")
            exit()
        return sys.argv[1]
