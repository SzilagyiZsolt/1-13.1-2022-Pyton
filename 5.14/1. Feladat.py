T=[0, 1, 2, 3, 4, 5, 6]
Mennyi=int(input("írj egy számot 0-tól 6-ig: "))
def nap(Mennyi):
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
    print(Mennyi)
nap(Mennyi)

