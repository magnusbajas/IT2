class Politiker:
    def __init__(self, politiker_ordbok) -> None:
        self.fornavn: str = politiker_ordbok["fornavn"]
        self.etternavn: str = politiker_ordbok["etternavn"]
        self.kjønn: str = "kvinne" if politiker_ordbok["kjoenn"] == 1 else "mann"
        self.fylke: str = politiker_ordbok["fylke"]["navn"]
        self.parti: str = politiker_ordbok["parti"]["navn"]
        self.parti_id: str = politiker_ordbok["parti"]["id"]
        self.verdi: int = 10_000
        self.komiteer: list[str] = [komite["navn"] for komite in politiker_ordbok["komiteer_liste"]]
        self.ukepoeng: list[int]

    def gi_ukepoeng(self, poeng: int):
        self.ukepoeng.append(poeng)
        
    def __str__(self) -> str:
        return f"{self.fornavn} {self.etternavn} ({self.parti_id}) {self.verdi}"
    



