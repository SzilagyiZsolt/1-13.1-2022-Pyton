T=[0, 1, 2, 3, 4, 5, 6]
Mikor=int(input("hányas számú napon indultál? "))
Mennyi=int(input("hány napig voltál távol? "))
while Mennyi>7:
    Mennyi=Mennyi-7
Mennyi=Mennyi+Mikor
for x in T:
    if Mennyi==0:
        Mennyi="Hétfő"
    elif Mennyi==1:
        Mennyi="Kedd"
    elif Mennyi==2:
        Mennyi="Szerda"
    elif Mennyi==3:
        Mennyi="Csütörtök"
    elif Mennyi==4:
        Mennyi="Péntek"
    elif Mennyi==5:
        Mennyi="Szombat"
    elif Mennyi==6:
        Mennyi="Vasárnap"
print("Ezen a napon térsz haza: ", Mennyi)