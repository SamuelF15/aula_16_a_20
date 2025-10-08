import requests
from pydantic import BaseModel

class PokemonSchame(BaseModel): 
    name: str
    type: list[str]

    class Config:
        from_attributes = True

def pegar_pokemon(id: int) -> PokemonSchame: 
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    data_types = data['types']
    types_list = [
        type_info['type']['name'] for type_info in data_types
    ]
    return PokemonSchame(name=data['name'], type=types_list)

pokemon = pegar_pokemon(6) # Exemplo com Charizard (id 6)

print(f"pokemon: {pokemon.name}   Tipo(s): {', ' .join(pokemon.type)}")
