import sys
from unittest.mock import Mock, patch

import pytest

from UserInterface import User_In
from View import View


@pytest.fixture
def user_in():
    return User_In()


def test_catch_intro_valid_argument(user_in):
    with patch.object(sys, "argv", ["script.py", "valid_param"]):
        result = user_in.catch_intro()
        assert result == "valid_param"


def test_catch_intro_no_arguments(user_in):
    mock_view = Mock(View)
    user_in.view = mock_view

    with patch.object(sys, "argv", ["script.py"]), pytest.raises(SystemExit):
        user_in.catch_intro()
        mock_view.alert.assert_called_once_with(
            "Parámetros no válidos. Se espera un único parámetro."
        )


def test_catch_intro_too_many_arguments(user_in):
    mock_view = Mock(View)
    user_in.view = mock_view

    with patch.object(sys, "argv", ["script.py", "param1", "param2"]), pytest.raises(
        SystemExit
    ):
        user_in.catch_intro()
        mock_view.alert.assert_called_once_with(
            "Parámetros no válidos. Se espera un único parámetro."
        )


def test_show(user_in):
    mock_view = Mock(View)
    user_in.view = mock_view

    output = ["actividad1", "actividad2"]
    user_in.show(output, "testuser")

    mock_view.header.assert_called_once_with(
        "Resumen de la actividad de testuser en GitHub/Events"
    )
    mock_view.info.assert_any_call("- actividad1")
    mock_view.info.assert_any_call("- actividad2")


def test_message(user_in):
    mock_view = Mock(View)
    user_in.view = mock_view

    user_in.message("Esto es un mensaje de prueba")

    mock_view.alert.assert_called_once_with("Esto es un mensaje de prueba")
