import turtle
kép=turtle.Screen()
Sanyi=turtle.Turtle()
kép.bgcolor("lightgreen")
Sanyi.color("hotpink")
Sanyi.pensize(3)
def négyzet(t, h):
    for x in range(5):
        t.forward(h)
        t.left(90)
meret=20
for x in range(5):
    négyzet(Sanyi, meret)
    Sanyi.right(90)
    Sanyi.penup()
    Sanyi.forward(15)
    Sanyi.pendown()
kép.mainloop()