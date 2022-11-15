import turtle
kép=turtle.Screen()
Eszti=turtle.Turtle()
kép.bgcolor("lightgreen")
Eszti.color("hotpink")
Eszti.pensize(3)
def sokszog_rajzolas(t, n, sz):
    for x in range(0,8):
        t.left(sz)
        t.forward(n)
sokszog_rajzolas(Eszti, 8, 50)
kép.mainloop()