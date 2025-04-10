from Pokemons import Pokemon
from dataclasses import dataclass

@ dataclass
class PokemonTeam:
        _members: set[Pokemon]
        _anotations: str = ""
        _format: str = "casual"
        
        @property
        def members(self) -> set[Pokemon]:
            return self._members

        @property
        def anotations(self) -> str:
            return self._anotations

        @property
        def format(self) -> str:
            return self._format
    
        