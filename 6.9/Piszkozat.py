import sys
def teszt(sikeres_teszt):
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z){0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z){0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

x1=int(input("Első szám: "))
y1=int(input("Második szám: "))
x2=int(input("Harmadik szám: "))
y2=int(input("Negyedik szám: "))
r=0
def meredekseg(y1,y2,x1,x2):
    if y1<y2 and x1<x2:
        return None
    elif y1<=y2 or x1<=x2:
        r=(y2-y1)/(x2-x1)
    print(r)
    return 0
if r<0:
    teszt(meredekseg(y1,y2,x1,x2)==None)
teszt(meredekseg(y1,y2,x1,x2)==r)