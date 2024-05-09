class Pokemon:

    def __init__(self, pokemon_ordbok) -> None:
        self.name: str = pokemon_ordbok["name"]["english"]
        self.id: int = pokemon_ordbok["id"]
        self.type: str = pokemon_ordbok["type"]
        self.hp: int = pokemon_ordbok["base"]["HP"]
        self.attack: int = pokemon_ordbok["base"]["Attack"]
        self.defense: int = pokemon_ordbok["base"]["Defense"]
        self.speed: int = pokemon_ordbok["base"]["Speed"]

    def __str__(self) -> str:
     return f"ID: {self.id}, Navn: {self.name}, Stats: {self.hp} {self.attack} {self.defense}"