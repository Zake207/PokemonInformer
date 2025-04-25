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
from Types import POKEMONSTATS
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
    def ConvertToFileFormat(self):
        """
        Converts Pokémon data to a formatted string suitable for file storage.
        Returns:
            str: Formatted string containing Pokémon details.
        """
        # file_name: str = self.data.name + '_'.join(random.choices('0123456789abcdef', k=10))
        file_contents: str = f'{self.data.name} @ {self.data.object}\n'
        file_contents += f'Ability: {self.data.ability}\n'
        file_contents += f'Tera Type: {self.stats.hptype}\n'
        file_contents += 'EVs: ' + ' / '.join(f'{self.stats.evs[stat]} {stat}' 
                                              for stat in POKEMONSTATS)
        file_contents += f'\n{self.stats.nature} Nature\n'
        file_contents += 'IVs: ' + ' / '.join(f'{self.stats.ivs[stat]} {stat}' 
                                              for stat in POKEMONSTATS)
        file_contents += f'\n- {self.moves[0].name}\n'
        file_contents += f'- {self.moves[1].name}\n'
        file_contents += f'- {self.moves[2].name}\n'
        file_contents += f'- {self.moves[3].name}\n'
        return file_contents
        

@dataclass
class PokemonDB(PokemonFile):
    pass

test = PokemonFile()
print(test.ConvertToFileFormat())
