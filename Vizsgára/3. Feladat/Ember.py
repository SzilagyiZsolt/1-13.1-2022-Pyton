from random import randint
from emberek_alap import Ember
T=[]
for x in range(3):
    a=input("Add meg a nevet!")
    b=input("Add meg a foglalkozást!")
    c=input("Add meg a nemét!(f/n)")
    szam=randint(0,50)
    if c=="f":
        c="férfi"
    elif c=="n":
        c="nő"
    T.append(Ember(a,b,c,szam))
for i in range(3):
    print(f"{T[i].getNEV()} {T[i].getNEM()}, {T[i].getFOG()}, szerencse száma a {T[i].getSZAM()}")