a=input("írj be egy szót vagy egy mondatot: ")
b=input("Mit szeretnél kicserélni? ")
c=input("Mire szeretnéd kicserélni? ")
def cserel(s, regi, uj):
    print(regi.split(s))
    print(uj.join(s))
cserel(a,b,c)
