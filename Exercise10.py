import turtle
movement = [(160, 20), (-43, 10), (270, 8), (-43, 12)]
window = turtle.Screen()
tess = turtle.Turtle()

for angle, steps in movement:
    tess.left(angle)
    tess.forward(steps)

window.mainloop()