import http.client
import json
import sys
from typing import List

import requests

from constants import USER_MSG
from View import View

view = View()


def catch_intro() -> str:

    if len[sys.argv] < 1 or len[sys.argv] > 2:
        view.alert("E")
        exit()
    data = sys.argv[1]
    return sys.argv[1:] if len(sys.argv) > 1 else []


def validate_argument():
    pass


# user reception
user_name = catch_intro()[0]


# Establece la conexión con GitHub
conn = http.client.HTTPSConnection("api.github.com")

# Forma la URL dinámica
url = f"/users/{user_name}/events"

# Define los headers (si estás usando autenticación)
headers = {
    "User-Agent": user_name,  # GitHub requiere un User-Agent
}

# Realiza la solicitud GET a la API
conn.request("GET", url, headers=headers)

# Obtiene la respuesta
response = conn.getresponse()
data = response.read()

# Decodifica los datos
repo_info = json.loads(data)
# DEBUGGING
# print(repo_info)
# print("typo del reporte", type(repo_info))
# print("tamaño: ")
# print(len(repo_info))
if repo_info == []:
    view.alert("No hay actividad reciente de ese usuario")
else:
    # verificación de si existe el usuario en GitHub
    # tambien puede hacerse por el campo status == 404
    if isinstance(repo_info, dict):
        if repo_info["message"] == "Not Found":
            view.alert(USER_MSG["USER_DONT_EXISTS"] + user_name)
        else:
            print("es un diccionario pero el mensaje NO es NO ENCONTRADO")
    else:
        view.info("lo recibido es una lista")
        print(repo_info)


# comprobar si hay actividad reciente

# print(repo_info)

# Cierra la conexión

conn.close()
conn.close()
