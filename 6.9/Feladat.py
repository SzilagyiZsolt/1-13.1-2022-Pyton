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
n=input("írj egy égtáj rövídítést: ")
def fordulj_orajarasi_iranyba(n):
    if n=="É":
        print("K")
        return n
    elif n=="Ny":
        print("É")
        return n
    elif n=="D":
        print("Ny")
        return n
    elif n=="K":
        print("D")
        return n
    elif n!="K" or "É" or "Ny" or "D":
        teszt(fordulj_orajarasi_iranyba(42) == None)
        return n
    elif n!="K" or "É" or "Ny" or "D":
        teszt(fordulj_orajarasi_iranyba(n) == None)
        return n
teszt(fordulj_orajarasi_iranyba(n) == n)


#2. Feladat
a=int(input("írj egy számot 0-tól 6-ig: "))
def nap_nev(a):
    if a==0:
        a="Hétfő"
        return a
    elif a==1:
        a="Kedd"
        return a
    elif a==2:
        a="Szerda"
        return a
    elif a==3:
        a="Csütörtök"
        return a
    elif a==4:
        a="Péntek"
        return a
    elif a==5:
        a="Szombat"
        return a
    elif a==6:
        a="Vasárnap"
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