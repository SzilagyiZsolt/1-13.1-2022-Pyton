
def könyv(oldal):
    if oldal>150:
        return True
    else:
        return False
a=input("Add meg a könyv címét! ")
b=int(input("Add meg az oldalainak számát! "))
while (a!=""):
    if könyv(b):
        print(f"A {a} hosszú terjedelmű könyv")
    else:
        print(f"A {a} rövid terjedelmű könyv")
    a=input("Add meg a könyv címét! ")
    b=int(input("Add meg az oldalainak számát! "))