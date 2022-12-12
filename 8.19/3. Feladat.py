gyumolcs = input("írj be egy gyümölcsöt!")
darab = 0
betu=input("Ird be a betűt amit számolni akarsz! ")
def karakter_szamlalas(a, b):
    for karakter in gyumolcs:
        if karakter == betu:
            darab=++1
    print(darab)
karakter_szamlalas(gyumolcs, darab)
