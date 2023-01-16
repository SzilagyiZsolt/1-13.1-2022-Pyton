class Ember():
    def __init__(self, nev, foglalkozas, nem, szam):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nem=nem
        self.szam=szam
    def neme(nem):
        if nem =="f":
            return "Férfi"
        elif nem == "n":
            return "Nő"