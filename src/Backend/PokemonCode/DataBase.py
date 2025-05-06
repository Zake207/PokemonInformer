from sqlite3 import connect
from Pokemons import PokemonFile
from json import dumps

class PokemonDB :
    def __init__(self, file: str = 'All'):
        self._db_path = './DataBase/PokemonDB/' + file + '.db'
        print(self._db_path)
        self._ensure_schema()
    
    def _connect(self):
        return connect(self._db_path)
    
    def _ensure_schema(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
            DB_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            ID INTEGER,
            Weight INTEGER,
            Height INTEGER,
            Ability TEXT,
            Type_1 TEXT,
            Type_2 TEXT,
            Object TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS moves (
            DB_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Pokemon_ID INTEGER,
            Move_1 TEXT,
            Move_2 TEXT,
            Move_3 TEXT,
            Move_4 TEXT,
            FOREIGN KEY(Pokemon_ID) REFERENCES pokemon(DB_ID) ON DELETE CASCADE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS stats (
            DB_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Pokemon_ID INTEGER,
            Base TEXT,
            Evs TEXT,
            Ivs TEXT,
            Stats TEXT,
            Nature TEXT,
            Hptype TEXT,
            FOREIGN KEY(Pokemon_ID) REFERENCES pokemon(DB_ID) ON DELETE CASCADE
        )
        """)

        conn.commit()
        conn.close()

    def SavePokemon(self, pokemon: PokemonFile):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO pokemon 
            (Name, ID, Weight, Height, Ability, Type_1, Type_2, Object) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", 
            (
                pokemon.data.name,
                pokemon.data.id,
                pokemon.data.weight,
                pokemon.data.height,
                pokemon.data.ability,
                pokemon.data.types[0],
                pokemon.data.types[1],
                pokemon.data.object,
            )
        )
        pokemon_db_id = cursor.lastrowid
        
        cursor.execute("""
            INSERT INTO moves (Pokemon_ID, Move_1, Move_2, Move_3, Move_4)
            VALUES (?, ?, ?, ?, ?)
            """, (pokemon_db_id, 
                  pokemon.moves[0], pokemon.moves[1], pokemon.moves[2], pokemon.moves[3]))
        
        cursor.execute("""
            INSERT INTO stats (Pokemon_ID, Base, Evs, Ivs, Stats, Nature, Hptype)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                pokemon_db_id,
                dumps(pokemon.stats.base),
                dumps(pokemon.stats.evs),
                dumps(pokemon.stats.ivs),
                dumps(pokemon.stats.stats),
                pokemon.stats.nature,
                pokemon.stats.hptype
            ))
        conn.commit()
        conn.close()
    
    def ShowAllPokemon(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                p.DB_ID, p.Name, p.ID, p.Weight, p.Height, p.Ability, p.Type_1, p.Type_2, p.Object,
                m.Move_1, m.Move_2, m.Move_3, m.Move_4, 
                s.Base, s.Evs, s.Ivs, s.Stats, s.Nature, s.Hptype
            FROM pokemon p
            LEFT JOIN moves m ON p.DB_ID = m.Pokemon_ID
            LEFT JOIN stats s ON p.DB_ID = s.Pokemon_ID
            """)
        result = cursor.fetchall()
        conn.close()
        return result

    def DeletePokemon(self, id: int):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pokemon WHERE DB_ID = ?", (id,))
        conn.commit()
        conn.close()
        
    def DeleteAll(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pokemon")
        conn.commit()
        conn.close()
    
    def GetAllPokemonEntries(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DB_ID, Name FROM pokemon
        """)
        results = cursor.fetchall()
        conn.close()
        return results
    
    def UpdateMetadata(self, id: int, atribute: str, valor: str):
        conn = self._connect()
        cursor = conn.cursor()
        match atribute:
            case 'Name':
               cursor.execute("UPDATE pokemon SET DB_ID = ? WHERE Name = ?", (id, valor))
            case 'ID':
               cursor.execute("UPDATE pokemon SET DB_ID = ? WHERE ID = ?", (id, str(valor)))
            case 'Weight':
               cursor.execute("UPDATE pokemon SET DB_ID = ? WHERE Weight = ?", (id, str(valor)))
            case 'Height':
               cursor.execute("UPDATE pokemon SET DB_ID = ? WHERE Height = ?", (id, str(valor)))
            case 'Ability':
               cursor.execute("UPDATE pokemon SET DB_ID = ? WHERE Ability = ?", (id, valor))
            case 'Type_1':
               cursor.execute("UPDATE pokemon SET DB_ID = ? WHERE Type_1 = ?", (id, valor))
            case 'Type_2':
               cursor.execute("UPDATE pokemon SET DB_ID = ? WHERE Type_2 = ?", (id, valor))
            case 'Object':
               cursor.execute("UPDATE pokemon SET DB_ID = ? WHERE Object = ?", (id, valor))
            case _:
                print('Unkown atribute.')
        conn.commit()
        conn.close()

pkm = PokemonFile()
db = PokemonDB()
db.DeleteAll()
db.SavePokemon(pkm)
print(db.ShowAllPokemon())


