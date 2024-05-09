from politiker import Politiker

class Fantasiparti:
    def __init__(self, navn: str, eier: str) -> None:
        self.navn: str = navn
        self.eier: str = eier
        self.poeng: int = 0
        self.saldo: int = 100_000
        self.partileder: Politiker = None
        self.politikere: list[Politiker] = []

    def print_politikere(self):
        # print politikerene i self.politikere, en politiker per linje
        if len(self.politikere) == 0:
            print("Partiet er tomt")
        else:
            for i in range(len(self.politikere)):
                print(f"{i}: {self.politikere[i]}")

    def kjøp_politiker(self, politiker: Politiker):
        if self.saldo >= politiker.verdi and politiker not in self.politikere:
            self.politikere.append(politiker) 
            self.saldo -= politiker.verdi

    def selg_politiker(self, politiker: Politiker):
        if politiker in self.politikere:
            self.politikere.remove(politiker)
            self.saldo += politiker.verdi
        