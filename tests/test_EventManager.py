import pytest

from EventManager import EventManager

from .constants_tests import (
    API_JSON,
    DICT_EVENT_REPO,
    EVENTS_MANAGER,
    OUTPUT_GENERATED,
    TUPLE_EVENT_REPO_COUNTER,
)


@pytest.fixture
def setup():
    return EventManager(API_JSON)


def test_data_conversion(setup):
    expected = EVENTS_MANAGER
    event_manager = setup
    assert expected == event_manager.get_events()


def test_analize_events(setup):
    expected = DICT_EVENT_REPO
    event_manager = setup
    assert expected == event_manager.analize_events()


def test_events_counter_repo(setup):
    expected = TUPLE_EVENT_REPO_COUNTER
    event_manager = setup
    data = event_manager.analize_events()
    assert expected == event_manager.events_counter_repo(data)


def test_generate_output(setup):
    expected = OUTPUT_GENERATED
    event_manager = setup
    data = event_manager.analize_events()
    data = event_manager.events_counter_repo(data)
    assert expected == event_manager.generate_output(data)
