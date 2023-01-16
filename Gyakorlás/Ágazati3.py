from emberek_alap import Ember
from random import randint
T=[]
a=input("Add meg a nevet! ")
b=input("Add meg a foglalkozását! ")
neme=input("Add meg a nemét! ")
szam=randint(0,50)
d=Ember(a,b,neme,szam)
print(f"{d.nev()} {d.nem()}, {d.foglalkozas()} szerencse száma a {d.szam()}")