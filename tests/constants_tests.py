from models.github import Actor, GitHubEvent, Repo

# FIXTURE: setup  (initialize event_manager)
API_JSON = [
    {
        "id": "41180088633",
        "type": "CreateEvent",
        "actor": {
            "id": 15149692,
            "login": "xerchion",
            "display_login": "xerchion",
            "gravatar_id": "",
            "url": "https://api.github.com/users/xerchion",
            "avatar_url": "https://avatars.githubusercontent.com/u/15149692?",
        },
        "repo": {
            "id": 845096649,
            "name": "xerchion/TaskTracker",
            "url": "https://api.github.com/repos/xerchion/TaskTracker",
        },
        "payload": {
            "ref": "main",
            "ref_type": "branch",
            "master_branch": "main",
            "description": "A command-line tool for managing tasks in a JSON file: add, update, mark, delete, and list tasks by status",
            "pusher_type": "user",
        },
        "public": True,
        "created_at": "2024-08-20T15:19:17Z",
    },
    {
        "id": "41179993047",
        "type": "CreateEvent",
        "actor": {
            "id": 15149692,
            "login": "xerchion",
            "display_login": "xerchion",
            "gravatar_id": "",
            "url": "https://api.github.com/users/xerchion",
            "avatar_url": "https://avatars.githubusercontent.com/u/15149692?",
        },
        "repo": {
            "id": 845096649,
            "name": "xerchion/TaskTracker",
            "url": "https://api.github.com/repos/xerchion/TaskTracker",
        },
        "payload": {
            "ref": None,
            "ref_type": "repository",
            "master_branch": "main",
            "description": "A command-line tool for managing tasks in a JSON file: add, update, mark, delete, and list tasks by status",
            "pusher_type": "user",
        },
        "public": True,
        "created_at": "2024-08-20T15:16:37Z",
    },
]

# TEST: test_data_conversion
EVENTS_MANAGER = [
    GitHubEvent(
        id="41180088633",
        type="CreateEvent",
        actor=Actor(
            id=15149692,
            login="xerchion",
            display_login="xerchion",
            url="https://api.github.com/users/xerchion",
        ),
        repo=Repo(
            id=845096649,
            name="xerchion/TaskTracker",
            url="https://api.github.com/repos/xerchion/TaskTracker",
        ),
        created_at="2024-08-20T15:19:17Z",
    ),
    GitHubEvent(
        id="41179993047",
        type="CreateEvent",
        actor=Actor(
            id=15149692,
            login="xerchion",
            display_login="xerchion",
            url="https://api.github.com/users/xerchion",
        ),
        repo=Repo(
            id=845096649,
            name="xerchion/TaskTracker",
            url="https://api.github.com/repos/xerchion/TaskTracker",
        ),
        created_at="2024-08-20T15:16:37Z",
    ),
]

# TEST: test_analize_events
DICT_EVENT_REPO = [
    {"CreateEvent": "xerchion/TaskTracker"},
    {"CreateEvent": "xerchion/TaskTracker"},
]
# TEST: events_counter_repo
TUPLE_EVENT_REPO_COUNTER = [({"CreateEvent": "xerchion/TaskTracker"}, 2)]

# TEST: generate_output
OUTPUT_GENERATED = [
    "Ha creado una rama o etiqueta de Git 2 veces en el repositorio: xerchion/TaskTracker"
]
