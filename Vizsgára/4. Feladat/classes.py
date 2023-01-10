class Menetlevél():
    def __init__(self, rendszám, megtett, fogyasztás):
        self.rendszám = rendszám
        self.megtett = megtett
        self.fogyasztás = fogyasztás
    def getREND(self):
        return self.rendszám
    def getMEG(self):
        return self.megtett
    def getFOGY(self):
        return self.fogyasztás