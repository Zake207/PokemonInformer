from Movements import Movement, Moveset
from Stats import PokemonStats
from Types import PokemonType, PokemonNature, HPTABLE, NATURESTATSEFFECT
from typing import Dict, Tuple
from dataclasses import dataclass


"""
The code below is used to declare and define de `Pokemon` class with its respective properties
"""




"""
CONFLICTO CON LA CLASE POKEMON
DEBERIA ALMACENAR TODOS LOS POSIBLES MOVIMIENTOS Y HABILIDADES O SOLO LOS QUE SE QUIERE USAR?

SI SE ELIGE LA 2: GUARDAR JUNTO A LA FICHA DE ESTE POKEMON UN JSON QUE TENGA TODAS LAS POSIBLES
OPCIONES PARA ESTE, Y CADA VEZ QUE SE QUIERA MODIFICAR SE HACE UN CHECK CON ESTE FICHERO PARA
CORROBORAR QUE ES VÁLIDO.

VALORAR UN PATRÓN DE DISEÑO CREACIONAL PARA SIMPLIFCAR

POSIBLE SOLUCIÓN, CONFIGURAR EL POKEMON Y HACER CONSULTAS PARA CORROBORAR LOS DATOS Y DAR ERROR O 
CREAR LA INSTACIA DEL POKEMON EN CUESTION
"""
@dataclass
class Pokemon:
        _name: str = "Missingno"
        _id: int = -1
        _weight: int = -1
        _height: int = -1
        _ability: str = "NULL" 
        _types: tuple[PokemonType, PokemonType] = ("NULL", "NULL")
        _moves: Moveset = None
        _object: str = "NULL"
        _stats: PokemonStats = None
        _nature: PokemonNature = "NULL"
        
        @classmethod
        def JsonImport(cls, file: str):
            pass
        
        @classmethod
        def JsonExport(cls, file: str):
            pass
        
        @property
        def name(self):
            return self._name
        
        @property
        def id(self):
            return self._id
        
        @property
        def weight(self):
            return self._weight
        
        @property
        def height(self):
            return self._height
        
        @property
        def ability(self):
            return self._ability
        
        @property
        def types(self):
            return self._types
        
        @property
        def moves(self):
            return self._moves
        
        @property
        def object(self):
            return self._object
        
        @property
        def nature(self):
            return self._nature
        
        @ability.setter
        def abilities(self, new_ability: str):
            self.ability = new_ability
        
        # EDITAR MOVIMIENTOS
        # EDITAR IVS, CON CALCULO DE HPTYPE INCLUIDO
        # EDITAR OBJETO
        @object.setter
        def object(self, new_object: str):
            self._object = new_object
        # EDITAR NATURALEZA
        @nature.setter
        def nature(self, new_nature: PokemonNature):
            self._nature = new_nature