import turtle
kép=turtle.Screen()
Sanyi=turtle.Turtle()
def szabalyos_haromszog_rajzolas(t, sz):
    t.left(120)
    t.forward(sz)
for x in range (3):
    szabalyos_haromszog_rajzolas(Sanyi, 100)
kép.mainloop()