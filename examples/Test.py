import sqlite3
import json
from typing import Dict

# Diccionario de ejemplo
evs: Dict[str, int] = {
    "Hp": 0,
    "Atk": 252,
    "Def": 0,
    "Satk": 0,
    "Sdef": 4,
    "Spd": 252
}

# Conexión a la base de datos
conn = sqlite3.connect("./examples/Test.db")
cur = conn.cursor()

# Crear tabla (si no existe)
cur.execute("""
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT,
    evs TEXT
);
""")

# Insertar un Pokémon con EVs serializados
cur.execute("""
INSERT INTO pokemon (name, evs) VALUES (?, ?)
""", ("Garchomp", json.dumps(evs)))  # json.dumps convierte el diccionario en una cadena JSON

conn.commit()

# Leer desde la base de datos y convertir EVs de nuevo a dict
cur.execute("SELECT id, name, evs FROM pokemon")
rows = cur.fetchall()
for row in rows:
    id, name, evs_json = row
    evs_dict = json.loads(evs_json)  # Convertimos de JSON a dict
    print(f"ID: {id}, Name: {name}, EVs: {evs_dict}")

conn.close()
