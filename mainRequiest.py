import json

from Api import Api
from Report import Report
from View import View

# ! FALTA LA ENTRADA DEL USUARIO Y SU VALIDACIÓN
user_name = "Xerchion"
api = Api(user_name)

view = View()
# Verifica que la solicitud fue exitosa
if api.is_conection_ok():
    # Convierte la respuesta a JSON
    data = api.extract_data()
    report = Report(data)
    show = report.get_events("CreateEvent")
    view.alert("Tamaño de la lista:" + str(len(show)))
    view.alert("-_" * 70)
    for el in show:
        print(el)

        view.info("-_" * 70)

    view.alert("-_" * 70)
    print(report.prepare_view())

    view.info(report.sumary())
    # Si deseas ver un ejemplo de evento
    if report:
        print("\nEjemplo de evento:")
        # Imprime el primer evento con indentación
        print("-" * 23)

    else:
        print("No se encontraron eventos.")

else:
    print(f"Error en la solicitud: {api.get_error()}")
