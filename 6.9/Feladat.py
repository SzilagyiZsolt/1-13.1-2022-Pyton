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
print("1. Feladat")
n=input("Írj be egy égtáj rövidítését: ")
def fordulj_orajarasi_iranyba(ég):
    if ég=="É":
        print("Szomszédos égtája: K")
        return ég
    elif ég=="Ny":
        print("Szomszédos égtája: É")
        return ég
    elif ég=="D":
        print("Szomszédos égtája: Ny")
        return ég
    elif ég=="K":
        print("Szomszédos égtája: D")
        return ég
    elif ég==int:
        ég==None
teszt(fordulj_orajarasi_iranyba(n) == n or fordulj_orajarasi_iranyba(n) != n)

#2. Feladat
print("2. Feladat")
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
    elif int:
        n==a
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

#3. Feladat (NEM JÓ)
print("3. Feladat")
a=input("írd be a hét egyik napját: ")
def nap_sorszam(nap):
    if nap=="Hétfő":
        nap=0
        print("Sorszáma:" ,nap)
        return nap
    elif nap=="Kedd":
        nap=1
        print("Sorszáma:" ,nap)
        return nap
    elif nap=="Szerda":
        nap=2
        print("Sorszáma:" ,nap)
        return nap
    elif nap=="Csütörtök":
        nap=3
        print("Sorszáma" ,nap)
        return nap
    elif nap=="Péntek":
        nap=4
        print("Sorszáma:" ,nap)
        return nap
    elif nap=="Szombat":
        nap=5
        print("Sorszáma:" ,nap)
        return nap
    elif nap=="Vasárnap":
        nap=6
        print("Sorszáma:" ,nap)
        return nap
    elif int:
        return nap
    elif a!="Hétfő" "Kedd" "Szerda" "Csütörtök" "Péntek" "Szombat" "Vasárnap":
        return None 
    elif a=="Hétfő" "Kedd" "Szerda" "Csütörtök" "Péntek" "Szombat" "Vasárnap":
        return nap
if a=="Hétfő":
    teszt(nap_sorszam(a) == 0)
elif a=="Kedd":
    teszt(nap_sorszam(a) == 1)
elif a=="Szerda":
    teszt(nap_sorszam(a) == 2)
elif a=="Csütörtök":
    teszt(nap_sorszam(a) == 3)
elif a=="Péntek":
    teszt(nap_sorszam(a) == 4)
elif a=="Szombat":
    teszt(nap_sorszam(a) == 5)
elif a=="Vasárnap":
    teszt(nap_sorszam(a) == 6)
elif int:
    teszt(nap_sorszam(nap_nev(a)) == a)
elif a=="Hétfő" "Kedd" "Szerda" "Csütörtök" "Péntek" "Szombat" "Vasárnap":
    teszt(nap_nev(nap_sorszam(a)) == a)
elif a!="Hétfő" "Kedd" "Szerda" "Csütörtök" "Péntek" "Szombat" "Vasárnap":
    teszt(nap_sorszam(a) ==None)

#4. Feladat
print("4. Feladat")
z=input("Milyen nap van? ")
y=int(input("Hány nap múlva szeretnél nyaralni? ")) 
x=0
if z=="Hétfő":
    z = 0
elif z=="Kedd":
    z = 1
elif z=="Szerda":
    z = 2
elif z=="Csütörtök":
    z = 3
elif z=="Péntek":
    z = 4
elif z=="Szombat":
    z = 5
elif z=="Vasárnap":
    z = 6
def napok_hozzaadasa(z,y):
    x = z+y
    while x>7:
        x=x-7
    if x==0:
        x = "Hétfő"
    elif x==1:
        x = "Kedd"
    elif x==2:
        x = "Szerda"
    elif x==3:
        x = "Csütörtök"
    elif x==4:
        x = "Péntek"
    elif x==5:
        x = "Szombat"
    elif x==6:
        x = "Vasárnap"
    print(x)
    return z+y==x
teszt(napok_hozzaadasa(z, y) == x)

#5. Feladat (Ez sem jó)
print("5. Feladat")
z=input("Milyen nap van? ")
y=int(input("Hány nap múlva szeretnél nyaralni? ")) 
x=0
if z=="Hétfő":
    z = 0
elif z=="Kedd":
    z = 1
elif z=="Szerda":
    z = 2
elif z=="Csütörtök":
    z = 3
elif z=="Péntek":
    z = 4
elif z=="Szombat":
    z = 5
elif z=="Vasárnap":
    z = 6
def napok_hozzaadasa(z,y):
    x = z+y
    while x<=0 and x<7:
        x=x%7
    if x==0:
        x = "Hétfő"
    elif x==1:
        x = "Kedd"
    elif x==2:
        x = "Szerda"
    elif x==3:
        x = "Csütörtök"
    elif x==4:
        x = "Péntek"
    elif x==5:
        x = "Szombat"
    elif x==6:
        x = "Vasárnap"
    
    print(x)
    return z-y==x
teszt(napok_hozzaadasa(z, y) == x)

#6. Feladat
print("6. Feladat")
a=input("Melyik hónapot választod? ")
def honap_napja(a):
    if a=="Január":
        print("A választott napod 31 napos!")
        return 31
    elif a=="Február":
        print("A választott napod 28 napos!")
        return 28
    elif a=="Március":
        print("A választott napod 31 napos!")
        return 31
    elif a=="Április":
        print("A választott napod 30 napos!")
        return 30
    elif a=="Május":
        print("A választott napod 31 napos!")
        return 31
    elif a=="Június":
        print("A választott napod 30 napos!")
        return 30
    elif a=="Július":
        print("A választott napod 31 napos!")
        return 31
    elif a=="Augusztus":
        print("A választott napod 31napos!")
        return 31
    elif a=="Szeptember":
        print("A választott napod 30 napos!")
        return 30
    elif a=="Október":
        print("A választott napod 31 napos!")
        return 31
    elif a=="November":
        print("A választott napod 30napos!")
        return 30
    elif a=="December":
        print("A választott napod 31 napos!")
        return 31
    elif int or a!="Január""Február""Március""Április""Május""Június""Július""Augusztus""Szeptember""Október""November""December":
        return None
if a=="Január":
    teszt(honap_napja(a) == 31)
elif a=="Február":
    teszt(honap_napja(a) == 28)
elif a=="Március":
    teszt(honap_napja(a) == 31)
elif a=="Április":
    teszt(honap_napja(a) == 30)
elif a=="Május":
    teszt(honap_napja(a) == 31)
elif a=="Június":
    teszt(honap_napja(a) == 30)
elif a=="Július":
    teszt(honap_napja(a) == 31)
elif a=="Augusztus":
    teszt(honap_napja(a) == 31)
elif a=="Szeptember":
    teszt(honap_napja(a) == 30)
elif a=="Október":
    teszt(honap_napja(a) == 31)
elif a=="November":
    teszt(honap_napja(a) == 30)
elif a=="December":
    teszt(honap_napja(a) == 31)
elif int or a!="Január""Február""Március""Április""Május""Június""Július""Augusztus""Szeptember""Október""November""December":
    teszt(honap_napja(a) == None)

#7. Feladat
print("7. Feladat")
a=int(input("Óra: "))
b=int(input("Perc: "))
c=int(input("Másodperc: "))
x=0
def masodpercre_valtas(a,b,c):
    a=a*3600
    b=b*60
    x=a+b+c
    print("Ennyi másodperc: ", x)
    return 0
teszt(masodpercre_valtas(a, b, c) == x)

#8. Feladat
print("8. Feladat")
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

#9. Feladat
print("9. Feladat")
q=int(input("Órára váltáshoz, add meg a másodpercet: "))
ú=0
ó=0
ű=0
k=0
p=0
def orakra_valtas(q):
    ú=q/3600
    print(int(ú), "óra")
    return 0
ó=q%3600
teszt(orakra_valtas(q) == ú)
def percekre_valtas(ó):
    ű=ó/60
    print(int(ű), "perc")
    return 0
teszt(percekre_valtas(ó) == ű)
def masodpercekre_valtas(ó):
    k=ó%60
    print(int(k), "másodperc")
    return 0
teszt(masodpercekre_valtas(ó) == k)

#10. Feladat
#teszt(3 % 4 == 0): Azért sikertelen mert nincs maradék
#teszt(3 % 4 == 3): Ez sikeres
#teszt(3 / 4 == 0): Azért sikertelen mert az érték 0.75
#teszt(3 // 4 == 0): Ez sikeres
#teszt(3+4*2 == 14): Azért sikertelen mert az érték nem egyenlő 14-el
#teszt(4-2+2 == 0): Azért sikertelen mert az érték nem egyenlő 0-val
#teszt(len("helló, világ!") == 13): Ez sikeres

#11. Feladat
print("11. Feladat")
a=int(input("írj be egy számot: "))
b=int(input("írj be egy másik számot: "))
def osszehasonlitas(a,b):
    if a>b:
        return 1
    elif a==b:
        return 0
    elif a<b:
        return -1
if a>b:
    teszt(osszehasonlitas(a, b) == 1)
elif a==b:
    teszt(osszehasonlitas(a, b) == 0)
elif a<b:
    teszt(osszehasonlitas(a, b) == -1)

#12. Feladat
print("12. Feladat")
a=int(input("írd be a befogót!"))
b=int(input("írd be a másik befogót!"))
c=0
def atfogo(u,p):
    c=a**2+b**2
    print(c**0.5)
    return 0
teszt(atfogo(a, b) == c)

#13. Feladat
print("13. Feladat")