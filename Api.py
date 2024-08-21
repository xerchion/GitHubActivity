import requests
from constants import ERROR_MSGS

class Api:
    def __init__(self, user):
        self.user = user

        self.url = f"https://api.github.com/users/{user}/events"
        self.headers = {"User-Agent": "mi_aplicacion"}
        self.response = self.get()
        self.error = self.response.status_code

    def get(self):
        # Realiza la solicitud GET a la API
        return requests.get(self.url, headers=self.headers)

    def is_conection_ok(self):
        return self.response.status_code == 200

    def extract_data(self):
        return self.response.json()

    def get_error(self):
        return ERROR_MSGS['initial'] + ERROR_MSGS[self.error]
