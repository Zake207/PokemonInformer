"""
Main module that defines the logic of a pokemon instance

Includes:
    + Base Class
    + File Convertion
    + DataBase Storage
"""
from typing import List
from Movements import Movement
from Stats import PokemonStats
from Metadata import Metadata
from dataclasses import dataclass, field
import random


"""
DECISIÓN DEL DISEÑO: CADA VEZ QUE SE QUIERA EDITAR UN POKEMON SE HACE USO DE LA API PARA CONSULTAR 
TODOS LOS MOVIMIENTO Y HABILIDADES QUE PUEDE TENER, GUARDARLOS EN UNA VARIABLE DE ENTORNO PARA SU
USO Y EVITAR HACER MAS CONSULTAS, DESPUES SE PUEDE GUARDAR EN UNA MEMORIA CACHE PARA EVITAR HACER
CONSULTAS A FUTURO
ADEMÁS LA MANERA DE SELECCIONAR MOVIMIENTOS PUEDE SER MOSTRAR UN DESPLEGABLE CON TODOS LOS MOVS DEL
POKEMON, FACILITANDO LA ELECCIÓN DE UN MOVIMIENTO VÁLIDO

AL GUARDAR LA SELECCIÓN SE HACEN LAS CONSULTAS DE LOS MOVIMIENTOS, LAS HABILIDAD, ETC...
"""


@dataclass
class PokemonBase:
    _data: Metadata = field(default_factory=Metadata)
    _moves: List[Movement] = field(default_factory=lambda: [Movement() for _ in range(4)])
    _stats: PokemonStats = field(default_factory=PokemonStats)

    @property
    def moves(self):
        return self._moves

    @property
    def data(self):
        return self._data

    @property
    def stats(self):
        return self._stats


@dataclass
class PokemonFile(PokemonBase):
    def ConvertToFile(self):
        file_name: str = self.data.name + '_'.join(random.choices('0123456789abcdef', k=10))
        with open(f'./Files/Pokemons/{file_name}', 'w') as file:
            file.write(f'{self.data.name} @ {self.data.object}')
            file.write(f'Ability: {self.data.ability}')
            file.write(f'Tera Type: {self.stats.hptype}')
        

@dataclass
class PokemonDB(PokemonFile):
    pass

test = PokemonFile()
test.ConvertToFile()
