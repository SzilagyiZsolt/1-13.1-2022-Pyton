import turtle
kép=turtle.Screen()
Sanyi=turtle.Turtle()
kép.bgcolor("lightgreen")
Sanyi.color("hotpink")
Sanyi.pensize(3)
def négyzet(t, h):
    for x in range(4):
        t.forward(h)
        t.left(90)
    Sanyi.penup()
    Sanyi.right(135)
    Sanyi.forward(15)
    Sanyi.right(135)
    Sanyi.pendown()
def négyzet2(a,b):
    for x in range(4):
        a.forward(b)
        a.right(90)
    Sanyi.penup()
    Sanyi.left(135)
    Sanyi.forward(15)
    Sanyi.left(135)
    Sanyi.pendown()
meret=20
for x in range(3):
    négyzet(Sanyi, meret)
    meret=meret+20
    négyzet2(Sanyi, meret)
    meret=meret+20
kép.mainloop()