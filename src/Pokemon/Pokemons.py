from Movements import Movement
from Types import PokemonType, PokemonNature, HPTABLE


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
        _ivs = (0, 0, 0, 0, 0, 0) # Hp Atk Def SAtk SDef Spd
        _base = (0, 0, 0, 0, 0, 0)
        _stats = (0, 0, 0, 0, 0, 0)
        _nature: PokemonNature = "NULL"
        _hptype = PokemonType
        
        @classmethod
        def JSON(cls, file: str):
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
        def evs(self):
            return self._evs
        
        @property
        def ivs(self):
            return self._ivs
        
        @property
        def base(self):
            return self._base
        
        @property
        def stats(self):
            return self._stats
        
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
        # EDITAR IVS, CON CALCULO DE HPTYPE INCLUIDO
        @property
        def _UpdateHpType(self):
            a = 0 if self.ivs[0] % 2 == 0 else 1
            b = 0 if self.ivs[1] % 2 == 0 else 1
            c = 0 if self.ivs[2] % 2 == 0 else 1
            d = 0 if self.ivs[5] % 2 == 0 else 1
            e = 0 if self.ivs[3] % 2 == 0 else 1
            f = 0 if self.ivs[4] % 2 == 0 else 1
            result = (a + 2*b + 4*c + 8*d + 16*e + 32*f) / 63
            self.hptype = HPTABLE[result]
            pass
        
        @property
        def _UpdateStats(self):
            pass
        
        @ivs.setter
        def ivs(self, new_ivs: list[int, int, int, int, int, int]):
            if len(new_ivs) != 6:
                raise ValueError("ERROR: You must introduce 6 integer numbers between 0 and 31.")
            for iv in new_ivs:
                if not iv in range(0,32):
                    raise ValueError("ERROR: iv's must be integer values between 0 and 31.")
            self.ivs = new_ivs
            self._UpdateHpType
            self._UpdateStats
        # EDITAR EVS
        @evs.setter
        def evs(self, new_evs: list[int, int, int, int, int, int]):
            if len(new_evs) != 6:
                raise ValueError("ERROR: You must introduce 6 integer numbers between 0 and 255.")
            for ev in new_evs:
                if not ev in range(0,256):
                    raise ValueError("ERROR: iv's must be integer values between 0 and 255.")
            self._UpdateStats
        # EDITAR OBJETO
        @object.setter
        def object(self, new_object: str):
            self._object = new_object
        # EDITAR NATURALEZA
        @nature.setter
        def nature(self, new_nature: PokemonNature):
            self._nature = new_nature