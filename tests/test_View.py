from unittest.mock import patch

import pytest
from pytest import fixture
from colorama import Fore

from src.View import View


@pytest.fixture
def view():
    return View()


@patch("builtins.print")
def test_alert(mock_print, view):
    view.alert("Alerta roja")

    assert mock_print.call_count == 3  # Se llama a print 3 veces: \n, msg, reset
    mock_print.assert_any_call("\n")
    mock_print.assert_any_call(Fore.RED + "Alerta roja")
    mock_print.assert_any_call(Fore.RESET)


@patch("builtins.print")
def test_info(mock_print, view):
    view.info("Información en azul")

    assert mock_print.call_count == 2  # Se llama a print 2 veces: msg, reset
    mock_print.assert_any_call(Fore.BLUE + "Información en azul")
    mock_print.assert_any_call(Fore.RESET)


@patch("builtins.print")
def test_reset(mock_print, view):
    view.reset()

    mock_print.assert_called_once_with(Fore.RESET)


@patch("builtins.print")
def test_header(mock_print, view):
    view.header("Encabezado del Reporte")

    assert (
        mock_print.call_count == 3
    )  # Se llama a print 3 veces: \n + header, info line
    mock_print.assert_any_call("\n" + Fore.BLUE + "Encabezado del Reporte")
    mock_print.assert_any_call(Fore.BLUE + "_" * 70)
    mock_print.assert_any_call(Fore.RESET)
