import sys
from unittest.mock import Mock, patch

import pytest

from src.constants import ACTIVITY_SUMMARY_TEXT, INVALID_PARAMETERS_MESSAGE
from src.UserInterface import UserInterface
from src.View import View


@pytest.fixture
def user_interface():
    return UserInterface()


def test_catch_intro_valid_argument(user_interface):
    with patch.object(sys, "argv", ["script.py", "valid_param"]):
        result = user_interface.catch_intro()
        assert result == "valid_param"


def test_catch_intro_no_arguments(user_interface):
    mock_view = Mock(View)
    user_interface.view = mock_view

    with patch.object(sys, "argv", ["script.py"]), pytest.raises(SystemExit):
        user_interface.catch_intro()
        mock_view.alert.assert_called_once_with(
            "Invalid parameters. A single parameter is expected."
        )


def test_catch_intro_too_many_arguments(user_interface):
    mock_view = Mock(View)
    user_interface.view = mock_view

    with patch.object(sys, "argv", ["script.py", "param1", "param2"]), pytest.raises(
        SystemExit
    ):
        user_interface.catch_intro()
        mock_view.alert.assert_called_once_with(INVALID_PARAMETERS_MESSAGE)


def test_show(user_interface):
    mock_view = Mock(View)
    user_interface.view = mock_view

    output = ["activity1", "activity2"]
    user_name = "testuser"
    user_interface.show(output, user_name)

    mock_view.header.assert_called_once_with(ACTIVITY_SUMMARY_TEXT + user_name)
    mock_view.info.assert_any_call("- activity1")
    mock_view.info.assert_any_call("- activity2")


def test_message(user_interface):
    mock_view = Mock(View)
    user_interface.view = mock_view

    user_interface.message("This is a test message")

    mock_view.alert.assert_called_once_with("This is a test message")
