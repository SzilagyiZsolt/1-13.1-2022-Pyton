a=int(input("írj be a befogót: "))
b=int(input("írj be egy másik befogót: "))
c=int(input("írj be az átfogót (ami a leghosszabb): "))
def derekszogu_e(a,b):
    if(a**2 + b**2 == c**2):
        print("Derékszög", a**2 + b**2 == c**2)
    elif (a**2 + b**2 != c**2):
        print("Nem derékszög", a**2 + b**2 == c**2)
derekszogu_e(a,b)