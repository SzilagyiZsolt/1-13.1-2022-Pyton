import sys
def teszt(sikeres_teszt):
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z){0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z){0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

s=int(input("Szám: "))
v=[3,0,5,11,2]
T=[]
def szorzas_skalarral(s, v):
    for x in range(len(v)):
        T.append(s*v[x])
    return T
szorzas_skalarral(s,v)
print(T)
teszt(szorzas_skalarral(s, v) == (T))