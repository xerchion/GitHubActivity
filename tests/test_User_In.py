import sys

import pytest  # type: ignore

from User_In import User_In


def test_no_params(monkeypatch, capsys):
    """Test para verificar que se lanza un mensaje de error y se llama a exit() cuando no se pasan parámetros."""
    # Simula no pasar parámetros
    monkeypatch.setattr(sys, "argv", ["script_name"])

    with pytest.raises(SystemExit):  # Captura el SystemExit
        User_In.catch_intro()

    # Captura el mensaje de alerta
    captured = capsys.readouterr()
    assert "Parámetros no válidos. Se espera un único parámetro." in captured.out


def test_correct_param(monkeypatch):
    """Test para verificar que se retorne el parámetro correcto cuando se pasa uno solo."""
    # Simula pasar un parámetro correcto
    monkeypatch.setattr(sys, "argv", ["main", "param1"])

    result = User_In.catch_intro()

    assert result == "param1"


def test_too_many_params(monkeypatch, capsys):
    """Test para verificar que se lanza un mensaje de error y se llama a exit() cuando se pasan más de un parámetro."""
    # Simula pasar más de un parámetro
    monkeypatch.setattr(sys, "argv", ["script_name", "param1", "param2"])

    with pytest.raises(SystemExit):  # Captura el SystemExit
        User_In.catch_intro()
