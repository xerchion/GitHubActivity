from unittest.mock import Mock, patch

import pytest

from Api import Api  # Asegúrate de que el nombre del módulo sea correcto
from constants import ERROR_MSGS


@pytest.fixture
def mock_response_200():
    """Mock para una respuesta con código 200."""
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"data": "some data"}
    return mock_resp


@pytest.fixture
def mock_response_404():
    """Mock para una respuesta con código 404."""
    mock_resp = Mock()
    mock_resp.status_code = 404
    mock_resp.json.return_value = {"message": "Not Found"}
    return mock_resp


@patch("requests.get")
def test_is_conection_ok(mock_get, mock_response_200):
    # Mockear la respuesta de requests.get
    mock_get.return_value = mock_response_200

    # Crear una instancia de Api
    api = Api("testuser")

    # Verificar que is_conection_ok es True cuando el código de estado es 200
    assert api.is_conection_ok() is True


@patch("requests.get")
def test_is_conection_not_ok(mock_get, mock_response_404):
    # Mockear la respuesta de requests.get
    mock_get.return_value = mock_response_404

    # Crear una instancia de Api
    api = Api("testuser")

    # Verificar que is_conection_ok es False cuando el código de estado es 404
    assert api.is_conection_ok() is False


@patch("requests.get")
def test_extract_data(mock_get, mock_response_200):
    # Mockear la respuesta de requests.get
    mock_get.return_value = mock_response_200

    # Crear una instancia de Api
    api = Api("testuser")

    # Verificar que extract_data devuelve los datos correctos
    assert api.extract_data() == {"data": "some data"}


@patch("requests.get")
def test_get_error(mock_get, mock_response_404):
    # Mockear la respuesta de requests.get
    mock_get.return_value = mock_response_404

    # Crear una instancia de Api
    api = Api("testuser")

    # Verificar que get_error devuelve el mensaje de error correcto
    expected_error = ERROR_MSGS["initial"] + ERROR_MSGS[404]
    assert api.get_error() == expected_error
