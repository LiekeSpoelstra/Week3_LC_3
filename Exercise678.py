import turtle
window = turtle.Screen()
drunk = turtle.Turtle()
heading = 0
turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for turn in turns:
    drunk.left(turn)
    drunk.forward(100)
    heading = heading + turn
final_heading = heading + 360
print(final_heading)
window.mainloop()

# answer to 8: a 20 degree angle