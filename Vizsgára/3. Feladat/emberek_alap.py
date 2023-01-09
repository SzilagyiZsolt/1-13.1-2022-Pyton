class Ember():
    def __init__(self, nev, foglalkozas, nem, szam):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nem = nem
        self.szam=szam
    def setSZAM(self, szam):
        self.szam=szam
    def setNEV(self, nev):
        self.nev=nev
    def setNEM(self, nem):
        self.nem=nem
    def setFOG(self, foglalkozas):
        self.foglalkozas=foglalkozas
    def getNEV(self):
        return self.nev
    def getNEM(self):
        return self.nem
    def getFOG(self):
        return self.foglalkozas
    def getSZAM(self):
        return self.szam

