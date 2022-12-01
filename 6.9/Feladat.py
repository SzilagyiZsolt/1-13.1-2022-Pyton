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
        ég==None
teszt(fordulj_orajarasi_iranyba(n) == n or fordulj_orajarasi_iranyba(n) != n)

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

#3. Feladat
a=input("írd be a hét egyik napját: ")
def nap_sorszám(nap):
    if nap=="hétfő" or "Hétfő":
        nap=0
        print("A Hétfőt választottad")
        return nap
    elif nap=="kedd" or "Kedd":
        nap=1
        print("A Keddet választottad")
        return nap
    elif nap=="szerda" or "Szerda":
        nap=2
        print("A Szerdát választottad")
        return nap
    elif nap=="csütörtök" or "Csütörtök":
        nap=3
        print("A Csütörtököt választottad")
        return nap
    elif nap=="péntek" or "Péntek":
        nap=4
        print("A Pénteket választottad")
        return nap
    elif nap=="szombat" or "Szombat":
        nap=5
        print("A Szombatot választottad")
        return nap
    elif nap=="vasárnap" or "Vasárnap":
        nap=6
        print("A Vasárnapot választottad")
        return nap
if a=="hétfő" or "Hétfő":
    teszt(nap_sorszám(a) == 0)
elif a=="kedd" or "Kedd":
    teszt(nap_sorszám(a) == 1)
elif a=="szerda" or "Szerda":
    teszt(nap_sorszám(a) == 2)
elif a=="csütörtök" or "Csütörtök":
    teszt(nap_sorszám(a) == 3)
elif a=="péntek" or "Péntek":
    teszt(nap_sorszám(a) == 4)
elif a=="szombat" or "Szombat":
    teszt(nap_sorszám(a) == 5)
elif a=="vasárnap" or "Vasárnap":
    teszt(nap_sorszám(a) == 6)