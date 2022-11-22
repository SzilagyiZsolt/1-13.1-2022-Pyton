xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
for x in xs:
    if x>90:
        x="Jeles"
    elif x>=80 and x <=90:
        x="Jó"
    elif x>=70 and x <=80:
        x="Közepes"
    elif x>=60 and x <=70:
        x="Elégséges"
    elif x<60:
        x="Elégtelen"
    print(f"Kapott jegyed: {x}")