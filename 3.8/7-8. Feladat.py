xs=[160, -43, 270, -97, -43, 200, -940, 17, -86]
import turtle
kép=turtle.Screen()
Kalóz=turtle.Turtle()
for x in xs:
    Kalóz.forward(100)
    if x>0:
        Kalóz.left(x)
    else:
        Kalóz.right(x)
összeg=0
for x in xs:
    if -360<x<360:
        x
    else:
        while -360<x<360:
            x
        else:
    összeg=összeg+x
print(f"Jelenleg {összeg} fokban áll a hajó")
kép.mainloop()