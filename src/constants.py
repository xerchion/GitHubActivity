# EventManager Constants
REPOSITORY_COUNT_TEXT = " times in the repository: "
NO_RECENT_ACTIVITY_MESSAGE = "There are no recent events for the user."
EVENTS_LONG_TEXT = {
    "CreateEvent": "Has created a Git branch or tag",
    "PushEvent": "Has pushed",
    "PullRequestEvent": "Has made pull requests",
    "IssueCommentEvent": "Has proposed changes or made comments",
    "PullRequestReviewEvent": "Reviews of pull requests",
    "IssuesEvent": "Has taken actions on issue reports",
    "GollumEvent": "Has created or updated a wiki page",
}

# UserInterface Constants
ACTIVITY_SUMMARY_TEXT = "Summary of activity in GitHub/Events for "
INVALID_PARAMETERS_MESSAGE = "Invalid parameters."

# API Constants
API_BASE_URL = "https://api.github.com/users/"
EVENTS_PAGE_PATH = "/events"
ERROR_MESSAGES = {
    "initial": "Error in the request:    ",
    "404": "There is no GitHub user with that name.",
    "UNKNOWN": "Unknown error",
}
