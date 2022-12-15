class Téglalap:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    
    def setA(self, a):
        self.a=a

    def setB(self, b):
        self.b=b

    def setAB(self, a, b):
        self.a=a
        self.b=b

    def getA(self):
        return self.a

    def getKerulet(self):
        return 2*(self.a+self.b)

    def getTerulet(self):
        return self.a * self.b