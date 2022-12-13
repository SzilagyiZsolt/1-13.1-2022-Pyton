def könyv(a):
    d=False
    if a<150:
        d=True
    return b
a=input("Add meg a könyv címét!")
while(a!=""):
    b=int(input("Add meg az oldalak számát!"))
    c=könyv(b)
    if c:
        print("A", a, "hosszú terjedelmű könyv")
    else:
        print("A", a, "rövid terjedelmű könyv")
    a=input("Add meg a könyv címét!")