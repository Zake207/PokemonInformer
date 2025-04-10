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