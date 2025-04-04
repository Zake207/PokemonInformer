from typing import Literal, Tuple

"""
The code below is used to declare and define de `Pokemon` class with its respective properties
"""

PokemonType = Literal["NULL", 
                      "normal", 
                      "fire", 
                      "water", 
                      "grass", 
                      "electric", 
                      "ice",
                      "fighting", 
                      "poison", 
                      "ground", 
                      "flying", 
                      "psychic", 
                      "bug",
                      "rock", 
                      "ghost", 
                      "dragon", 
                      "dark", 
                      "steel", 
                      "fairy"]

Nature = Literal["adamant", "bashful", "bold", "brave", "calm", "careful", 
    "docile", "gentle", "hasty", "hardy", "impish", "jolly", 
    "lax", "lonely", "mild", "modest", "naive", "naughty", 
    "quiet", "quirky", "rash", "relaxed", "sassy", "serious", 
    "timid"
]

class Pokemon:
        _name: str = "Missingno"
        _id: int = -1
        _weight: int = -1
        _height: int = -1
        _abilities: tuple[str, str, str] = ("NULL", "NULL", "NULL")
        _types: tuple[PokemonType, PokemonType] = ("NULL", "NULL")
        _moves: tuple[str, ...] = []
        _object: str = "NULL"
        _evs = (0, 0, 0, 0, 0, 0)
        _ivs = (0, 0, 0, 0, 0, 0)
        _nature = "NULL"
        _hpype = PokemonType
        pass

        