from classes import Menetlevél
r=open("fogyasztas.txt", "r", encoding="utf-8")
T=[]

for line in r:
        a=line.split(";")
        b=Menetlevél(a[0])
        a.setMEG(int(a[1]))
        b.setFOGY(float(a[2][0:len(a[2])-2]))
        T.append(b)
r.close()

r=open("atlagfogyasztas.txt", "w")
for a in b:
        r.write(f"{a.getREND()},{a.atlagfogyasztas()}\n")
        print(f"{a.getREND()},{a.atlagfogyasztas()}\n")
r.close()