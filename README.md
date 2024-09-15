# Proyecto: Consumir y pintar una API con Python

## Descripción

Este proyecto proporciona un ejemplo básico de cómo conectar una aplicación Python a una API en formato JSON y obtener los datos utilizando la biblioteca `requests`. El código muestra cómo ejecutar una consulta simple y recuperar resultados de la respuesta en formato JSON utilizando la biblioteca `json`.

## Estructura de Archivos

- `main.py`: Archivo principal que establece la conexión a la API y ejecuta una consulta.
- `payload.json`: Archivo con el formato de salida que obtendremos al consultar la API.

## Requisitos

- Python 3.12.3
- Paquetes instalados:
  - `requests`
  - `pip`

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/lvildoza/python_json_parse.git
   cd tu-repositorio
   ```

2. Instala los paquetes necesarios:
   ```bash
   pip install requests
   ```

## Contenido del Proyecto

### `main.py`

```python
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
```

### `payload.json`

```JSON
{
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
    }
}
```

## Ejecución

Para ejecutar el proyecto, simplemente ejecuta `main.py`:

```bash
python main.py
```

Deberías ver un mensaje con la respuesta de la consulta a la API "Los datos son: Usuario - Bret, con dirreción en: calle - Kulas Light" si todo está configurado correctamente.
