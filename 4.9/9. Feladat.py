import turtle
kép=turtle.Screen()
Sanyi=turtle.Turtle()
Sanyi.pensize(3)
def csillag(t):
    for x in range (5):
        t.right(144)
        t.forward(100)
csillag(Sanyi)
kép.mainloop()