a=int(input("Adj meg egy számot! "))
b=int(input("Add meg a második számot! "))
if a<0 and b>0:
    print("A két szám közül az első negatív")
elif b<0 and a>0:
    print("A két szám közül a második negatív")
elif a<0 and b<0:
    print("A mind a két szám negatív")
else:
    print("A két szám közül egyik sem negatív")