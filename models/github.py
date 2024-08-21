from typing import List, Optional

from pydantic import BaseModel  # type: ignore


class Actor(BaseModel):
    id: int
    login: str
    display_login: Optional[str]
    url: str


class Repo(BaseModel):
    id: int
    name: str
    url: str


class GitHubEvent(BaseModel):
    id: str
    type: str
    actor: Actor
    repo: Repo
    created_at: str


class GitHubEventsResponse(BaseModel):
    events: List[GitHubEvent]
