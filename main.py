"""
JSON = JavaScript Object Notation
"""
import requests
import json

# Realiza la solicitud a la API
response = requests.get('https://jsonplaceholder.typicode.com/users/1')

# Convierte la respuesta a un diccionario de Python
response_json = response.json()

# Obtiene los datos del usuario y la calle
user = response_json['username']
street = response_json['address']['street']

# Imprime los datos
print(f"Los datos son: Usuario - {user}, con dirreción en: calle - {street}")
