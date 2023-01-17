info=open("info.txt", "r", encoding="utf-8")
a=info.readline()
for row in info:
    if "info" in a:
        T=info.read()
print(T)
info.close()