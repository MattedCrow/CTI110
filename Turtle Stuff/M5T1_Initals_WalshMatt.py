# CTI 110
# M5T1 Turtle Graphics - Initals Edition
# Matthew 'Melissa' Walsh
# 10.12.17
# Fun with Turtles! This program draws using turtle graphics

# Initalize Turtles
import turtle
wn = turtle.Screen()
remi = turtle.Turtle()

# M method
def drawM():

    remi.left(90)
    remi.forward(100)
    remi.right(140)
    remi.forward(50)
    remi.left(100)
    remi.forward(50)
    remi.right(140)
    remi.forward(100)

# W method
def drawW():

    remi.left(180)
    remi.forward(100)
    remi.left(140)
    remi.forward(50)
    remi.right(100)
    remi.forward(50)
    remi.left(140)
    remi.forward(100)

# Main method
def main():
    # Draw an M
    drawM()

    # Move the Pen    
    remi.penup()
    remi.left(90)
    remi.forward(50)
    remi.left(90)
    remi.forward(100)
    remi.pendown()

    # Draw a W
    drawW()

    # Wait for user
    wn.mainloop()

# Program Start
main()
