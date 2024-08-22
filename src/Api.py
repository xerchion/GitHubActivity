from typing import Any

import requests

from src.constants import API_BASE_URL, ERROR_MESSAGES, EVENTS_PAGE_PATH


class Api:
    def __init__(self, user: str):
        self.user = user
        self.url = f"{API_BASE_URL }{user}{EVENTS_PAGE_PATH}"
        self.headers = {"User-Agent": "mi_aplicacion"}
        self.response = None
        self.error = None

    def _make_request(self) -> requests.Response:
        # Make the GET request to the API
        return requests.get(self.url, headers=self.headers)

    def is_connection_ok(self) -> bool:
        # Check if the request was successful (200 OK)
        if not self.response:
            self.response = self._make_request()
        return self.response.status_code == 200

    def extract_data(self) -> Any:
        # Extract and return the JSON data from the response
        if not self.response:
            self.response = self._make_request()
        return self.response.json()

    def get_error(self) -> str:
        # Get a user-friendly error message based on the status code
        if not self.response:
            self.response = self._make_request()
        self.error = str(self.response.status_code)
        return ERROR_MESSAGES["initial"] + ERROR_MESSAGES.get(self.error, "UNKNOWN")
