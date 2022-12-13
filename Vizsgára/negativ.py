a=int(input("Adj meg egy számot!"))
b=int(input("Adj meg a második számot!"))
if a > 0 and b > 0:
    print("A két szám közül egyik sem negatív")
elif a > 0 and b < 0:
    print("A két szám közül a második negatív")
elif a < 0 and b > 0:
    print("A két szám közül az első negatív")
elif a < 0 and b < 0:
    print("A mind a két szám negatív")