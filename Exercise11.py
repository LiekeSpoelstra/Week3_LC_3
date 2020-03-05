import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.speed(1)
movements = [(45, 100), (90, 50), (90, 50), (90, 100), (135, 70), (90, 71), (90, 70), (90, 70)]
for angle, steps in movements:
    tess.left(angle)
    tess.forward(steps)

window.mainloop()