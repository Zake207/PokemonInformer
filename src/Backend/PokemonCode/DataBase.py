from sqlite3 import connect
from Pokemons import PokemonFile

class PokemonDB :
    def __init__(self):
        self._db_path = './DataBase/PokemonDB/All.db'
        self._ensure_schema()
    
    def _connect(self):
        return connect(self._db_path)
    
    def _ensure_schema(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT
        )""")

        conn.commit()
        conn.close()

    def save(self, pokemon: PokemonFile):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO pokemon (Name) VALUES (?)""", (
            pokemon.data.name,
        ))
        conn.commit()
        conn.close()

pkm = PokemonFile()
db = PokemonDB()
db.save(pkm)

