import os
import sys
import json
from pokemon import Pokemon 

# 1. Oppsett

def rens_terminal():
    if sys.platform == "Windows" or sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

with open("pokemon.json", "r", encoding ="UTF-8") as fil:
    pokemoner = json.load(fil)

pokemon_liste = [] # lager tom liste
for pokemon in pokemoner: # går igjennom listen "pokemon_liste"
    ny_pokemon = Pokemon(pokemon) # henter info fra klassen Pokemon
    pokemon_liste.append(ny_pokemon) # legger den infoen in i listen "pokemon_liste"


# 2. Gameloop 

while True:
    rens_terminal()
    print("1: Se pokemonoversikt")
    print("2: Se treneroversikt")
    print("3: Lag trener")
    print("4: Avslutt")

    brukervalg = input("> ")
    rens_terminal()
    if brukervalg == "1":
        for pokemon in pokemon_liste:
            print(pokemon)
    
    elif brukervalg == "3":
        print("Hva vil du kalle treneren din?")
        trener_navn = input("> ")
        

    print("Trykk enter for å fortsette")
    input()
