from datetime import datetime
from typing import Any, Dict


class Event:
    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id")
        self.type = data.get("type")
        self.actor = data.get("actor", {})
        self.repo = data.get("repo", {})
        self.payload = data.get("payload", {})
        self.public = data.get("public", False)
        self.created_at = self.parse_created_at(data.get("created_at", ""))

    def parse_created_at(self, created_at: str) -> datetime:
        """Parse the 'created_at' field to a datetime object."""
        try:
            return datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            return (
                datetime.min
            )  # Valor predeterminado si el formato de fecha es incorrecto

    def __repr__(self) -> str:
        return (
            f"Event(id={self.id}, type={self.type}, actor={self.actor}, "
            f"repo={self.repo}, payload={self.payload}, public={self.public}, "
            f"created_at={self.created_at.isoformat()})"
        )

    def get_name(self):
        return self.type


# Ejemplo de uso
event_data = {
    "id": "1234567890",
    "type": "PushEvent",
    "actor": {"id": "1", "login": "octocat"},
    "repo": {"id": "2", "name": "octocat/hello-world"},
    "payload": {
        "push_id": "1",
        "size": 1,
        "distinct_size": 1,
        "ref": "refs/heads/main",
    },
    "public": True,
    "created_at": "2024-08-20T10:00:00Z",
}
