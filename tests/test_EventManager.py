import pytest

from src.EventManager import EventManager

from .constants_tests import (
    API_JSON,
    EVENT_REPO_COUNT_TUPLES,
    EVENT_REPO_DICTIONARIES,
    EVENTS_MANAGER,
    GENERATED_OUTPUT,
)


@pytest.fixture
def setup():
    return EventManager(API_JSON)


def test_data_conversion(setup):
    expected = EVENTS_MANAGER
    event_manager = setup
    assert expected == event_manager.get_events()


def test_analize_events(setup):
    expected = EVENT_REPO_DICTIONARIES
    event_manager = setup
    assert expected == event_manager.analize_events()


def test_events_counter_repo(setup):
    expected = EVENT_REPO_COUNT_TUPLES
    event_manager = setup
    data = event_manager.analize_events()
    assert expected == event_manager.events_counter_repo(data)


def test_generate_output(setup):
    expected = GENERATED_OUTPUT
    event_manager = setup
    data = event_manager.analize_events()
    data = event_manager.events_counter_repo(data)
    assert expected == event_manager.generate_output(data)
