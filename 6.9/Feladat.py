import sys
def teszt(sikeres_teszt):
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z){0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z){0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

def abszolut_ertek(n):
    if n < 0:
        return 1
    elif n > 0:
        return n

#1. Feladat
n=input("Írj be egy égtáj rövidítését: ")
def fordulj_orajarasi_iranyba(ég):
    if ég=="É":
        print("K")
        return ég
    elif ég=="Ny":
        print("É")
        return ég
    elif ég=="D":
        print("Ny")
        return ég
    elif ég=="K":
        print("D")
        return ég
    elif ég==int:
        ég == None
if 
teszt(fordulj_orajarasi_iranyba(n) == n)

#2. Feladat
a=int(input("írj egy számot 0-tól 6-ig: "))
def nap_nev(a):
    if a==0:
        a="Hétfő"
        print("A Hétfőt választottad")
        return a
    elif a==1:
        a="Kedd"
        print("A Keddet választottad")
        return a
    elif a==2:
        a="Szerda"
        print("A Szerdát választottad")
        return a
    elif a==3:
        a="Csütörtök"
        print("A Csütörtököt választottad")
        return a
    elif a==4:
        a="Péntek"
        print("A Pénteket választottad")
        return a
    elif a==5:
        a="Szombat"
        print("A Szombatot választottad")
        return a
    elif a==6:
        a="Vasárnap"
        print("A Vasárnapot választottad")
        return a
if a==0:
    teszt(nap_nev(a) == "Hétfő")
elif a==1:
    teszt(nap_nev(a) == "Kedd")
elif a==2:
    teszt(nap_nev(a) == "Szerda")
elif a==3:
    teszt(nap_nev(a) == "Csütörtök")
elif a==4:
    teszt(nap_nev(a) == "Péntek")
elif a==5:
    teszt(nap_nev(a) == "Szombat")
elif a==6:
    teszt(nap_nev(a) == "Vasárnap")
elif a>6:
    teszt(nap_nev(a) == None)