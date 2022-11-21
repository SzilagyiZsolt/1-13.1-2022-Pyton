T=[0, 1, 2, 3, 4, 5, 6]
def napok(napok):
    for x in T:
        if x==0:
            Mennyi="Hétfő"
        if x==1:
            Mennyi="Kedd"
        if x==2:
            Mennyi="Szerda"
        if x==3:
            Mennyi="Csütörtök"
        if x==4:
            Mennyi="Péntek"
        if x==5:
            Mennyi="Szombat"
        if x==6:
            Mennyi="Vasárnap"

Mikor=int(input("hányas számú napon indultál "))
Mennyi=int(input("hány napig voltál távol "))
while Mennyi>7:
    Mennyi=Mennyi-7
Mennyi=Mennyi+Mikor
napok(6)
print(Mennyi)