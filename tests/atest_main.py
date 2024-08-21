from unittest.mock import Mock, patch

import pytest


# Test de funcionalidad completa
@patch("Api.Api", autospec=True)
@patch("EventManager.EventManager", autospec=True)
@patch("UserInterface.User_In", autospec=True)
def test_funcionalidad_completa(mock_user_in, mock_event_manager, mock_api, capfd):
    # Configurar el mock para User_In
    mock_user_in_instance = mock_user_in.return_value
    mock_user_in_instance.catch_intro.return_value = "test_user"

    # Configurar el mock para Api
    mock_api_instance = mock_api.return_value
    mock_api_instance.is_conection_ok.return_value = True
    mock_api_instance.extract_data.return_value = [
        {"type": "PushEvent", "repo": {"name": "test_repo"}}
    ]
    mock_api_instance.get_error.return_value = "Error"

    # Configurar el mock para EventManager
    mock_event_manager_instance = mock_event_manager.return_value
    mock_event_manager_instance.analize_events.return_value = {
        "test_repo": ["PushEvent"]
    }
    mock_event_manager_instance.events_counter_repo.return_value = {"test_repo": 1}
    mock_event_manager_instance.generate_output.return_value = [
        "PushEvent occurred in test_repo"
    ]

    # Simula la ejecución del script
    from main import api, event_manager, user_interface, user_name

    user_name = mock_user_in_instance.catch_intro()

    # Ejecutar el flujo completo
    if api.is_conection_ok():
        analized = event_manager.analize_events()
        resume_list_events = event_manager.events_counter_repo(analized)
        output = event_manager.generate_output(resume_list_events)
        user_interface.show(output, user_name)
    else:
        user_interface.message(api.get_error())

    # Capturar la salida de la consola
    captured = capfd.readouterr()

    # Verificar que la salida es la esperada
    assert "Resumen de la actividad de test_user en GitHub/Events" in captured.out
    assert "- PushEvent occurred in test_repo" in captured.out
