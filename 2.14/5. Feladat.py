c=10000
r=8
m=12
t=int(input("Hány év?"))
mt=m+t
FV=c*(1+r/m)**mt
print(FV)