import sys
def teszt(sikeres_teszt):
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z){0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z){0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

a=float(input("Óra: "))
b=float(input("Perc: "))
c=float(input("Másodperc: "))
x=0
def masodpercre_valtas(a,b,c):
    a=a*3600
    b=b*60
    x=a+b+c
    print("Ennyi másodperc: ", int(x))
    return 0
teszt(masodpercre_valtas(a, b, c) == x)