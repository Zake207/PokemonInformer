from Movements import Movement
from Types import PokemonType, PokemonNature
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
        _moves: tuple[Movement, Movement, Movement, Movement] = ["NULL", "NULL", "NULL", "NULL"]
        _object: str = "NULL"
        _evs = (0, 0, 0, 0, 0, 0)
        _ivs = (0, 0, 0, 0, 0, 0)
        _nature: PokemonNature = "NULL"
        _hptype = PokemonType
        
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
        def evs(self):
            return self._evs
        
        @property
        def ivs(self):
            return self._ivs
        
        @property
        def nature(self):
            return self._nature
        
        @property
        def hptype(self):
            return self._hptype
        
        @ability.setter
        def abilities(self, new_ability: str):
            self.ability = new_ability
        
        # EDITAR MOVIMIENTOS
        # EDITAR EVS, CON CALCULO DE HPTYPE INCLUIDO
        # EDITAR IVS
        # EDITAR OBJETO
        # EDITAR NATURALEZA
        
        
        
        
        
        

        