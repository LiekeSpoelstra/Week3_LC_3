import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.color("black")
alex = turtle.Turtle()
alex.color("green")
peter = turtle.Turtle()
peter.color("purple")
tom = turtle.Turtle()
tom.color("blue")
for _ in range(3):
    tess.forward(50)
    tess.left(120)
for _ in range(4):
    alex.forward(60)
    alex.left(90)
for _ in range(6):
    peter.forward(70)
    peter.left(60)
for _ in range(8):
    tom.forward(80)
    tom.left(45)

window.mainloop()