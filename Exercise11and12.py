import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.stamp()

for _ in range (12):
    tess.penup()
    tess.hideturtle()
    tess.forward(100)
    tess.stamp()
    tess.forward(-100)
    tess.right(30)

window.mainloop()

print(type(tess))

