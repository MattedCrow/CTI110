# CTI 110
# M5T1 Turtle Graphics - Shapes Edition
# Matthew 'Melissa' Walsh
# 10.12.17
# Fun with Turtles! This program draws using turtle graphics

# Initalize Turtles
import turtle
wn = turtle.Screen()
remi = turtle.Turtle()

# Square
def drawSquare():

    for x in range(0,4):
        remi.forward(100)
        remi.left(90)

def drawTriangle():

    for x in range(0,3):
        remi.forward(100)
        remi.right(120)

def main():
    # Draw a Square
    drawSquare()

    # Change color to green
    remi.color("green")

    # Draw a Triangle
    drawTriangle()

    # Wait for user
    wn.mainloop()

# Program Start
main()
