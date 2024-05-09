from pokemon import Pokemon

class Trener:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.pokemon_liste: list[Pokemon] = []

    def legg_til_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemon_liste:
           self.pokemon_liste.append(pokemon)
    
    def fjern_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon_liste:
           self.pokemon_liste.remove(pokemon)
           
    def __str__(self) -> str:
     return f"Trener {self.name} har {len(self.pokemon_liste)} pokemon "¨