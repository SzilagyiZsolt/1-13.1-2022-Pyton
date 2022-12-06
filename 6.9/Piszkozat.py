import sys
def teszt(sikeres_teszt):
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z){0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z){0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

q=int(input("Órára váltáshoz, add meg a másodpercet: "))
ú=0
ó=0
ű=0
k=0
p=0
def orakra_valtas(q):
    ú=q/3600
    print(int(ú))
ó=q%3600
print(int(ó))
teszt(orakra_valtas(q) == ú)
def percekre_valtas(ó):
    ű=ó/60
    print(int(ű))
k=ű%60
print(int(k))
teszt(percekre_valtas(ó) == ű)
