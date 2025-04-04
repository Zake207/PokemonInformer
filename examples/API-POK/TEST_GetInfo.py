import requests
import json

pokemon: str = input("Introduzca el nombre del pokemon a consultar ")
URL = "https://pokeapi.co/api/v2/pokemon/" + pokemon

try:
    response = requests.get(URL)
    data = response.json()
    print(f"Nombre: {data['name']}")
    print(f"ID: {data['id']}")
    print(f"Altura: {data['height']}")
    print(f"Peso: {data['weight']}")
    # ESCRIBE EN FICHERO PARA VER FORMATO
    # with open ("data.json", "w", encoding="utf-8") as file:
    #     json.dump(data, file, indent=4)
except requests.exceptions.HTTPError as http_err:
    print(f"❌ Error HTTP: {http_err}")  # Error 404, 500, etc.
except requests.exceptions.ConnectionError:
    print("❌ Error de conexión. Verifica tu internet.")
except requests.exceptions.Timeout:
    print("⏳ La solicitud tardó demasiado. Intenta de nuevo.")
except requests.exceptions.RequestException as err:
    print(f"⚠️ Error desconocido: {err}")
