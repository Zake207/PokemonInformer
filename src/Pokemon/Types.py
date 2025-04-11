from typing import Literal

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

PokemonNature = Literal["NULL", "adamant", "bashful", "bold", "brave", "calm", "careful", 
    "docile", "gentle", "hasty", "hardy", "impish", "jolly", 
    "lax", "lonely", "mild", "modest", "naive", "naughty", 
    "quiet", "quirky", "rash", "relaxed", "sassy", "serious", 
    "timid"
]

PokemonAttackCategory = Literal ["NULL", "physical", "special", "status"]

PokemonAttackObjetive = Literal ["NULL", "single", "area", "itself", "partner"]

HPTABLE = [
    "fighting",   # 0
    "flying",     # 1
    "poison",     # 2
    "ground",     # 3
    "rock",       # 4
    "bug",        # 5
    "ghost",      # 6
    "steel",      # 7
    "fire",       # 8
    "water",      # 9
    "grass",      # 10
    "electric",   # 11
    "psychic",    # 12
    "ice",        # 13
    "dragon",     # 14
    "dark"        # 15
]