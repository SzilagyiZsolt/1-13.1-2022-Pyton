import turtle
kép=turtle.Screen()
Sanyi=turtle.Turtle()
Sanyi.pensize(3)
Sanyi.color("hotpink")
kép.bgcolor("lightgreen")
def csillag(t):
    for x in range(5):
        for x in range (5):
            t.right(144)
            t.forward(100)
        t.penup()
        t.forward(650)
        t.right(144)
        t.pendown()
csillag(Sanyi)
kép.mainloop()

#Ha nem emelem fel a tollat, akkor egy nagy csillagot kapok