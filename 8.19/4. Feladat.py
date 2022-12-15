gyumolcs = input("írj be egy gyümölcsöt!")
darab = 0
betu=input("Ird be a betűt amit számolni akarsz! ")
def karakter_szamlalas(gyumolcs, darab, betu):
    for karakter in gyumolcs:
        if karakter == betu:
            darab=gyumolcs.find(betu)
    print(darab)
karakter_szamlalas(gyumolcs, darab, betu)