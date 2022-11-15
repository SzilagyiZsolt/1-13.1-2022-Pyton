import turtle
kép=turtle.Screen()
Sanyi=turtle.Turtle()
kép.bgcolor("lightgreen")
Sanyi.color("blue")
def megy(t, h):
    t.right(89)
    t.forward(h)
meret=1
for x in range(100):
    megy(Sanyi, meret)
    meret=meret+1
kép.mainloop()