# CTI 110
# M5T1 Turtle Graphics - Bonus Snowflake Edition
# Matthew 'Melissa' Walsh
# 10.12.17
# Fun with Turtles! This program draws using turtle graphics

# Initalize Turtles
import turtle
wn = turtle.Screen()
remi = turtle.Turtle()
remi.speed(10)
remi.color("green")

noah = turtle.Turtle()
noah.color("purple")
noah.speed(10)


# Snowflake method 1
def drawFlake1():
    for x in range(0,12):
        remi.forward(150)
        remi.right(150)

# Snowflake method 2
def drawFlake2():
    for x in range(0,22):
        remi.right(50)        
        for x in range(0,3):
            remi.forward(120)
            remi.right(120)
        noah.right(50)
        for x in range(0,5):
            noah.forward(100)
            noah.left(140)

# Main method
def main():
    # Draw a snowflake
    drawFlake1()

    # Move Turtles
    remi.penup()
    remi.left(180)
    remi.forward(200)
    remi.pendown()
    noah.penup()
    noah.left(180)
    noah.forward(183)
    noah.pendown()

    # Draw another snowflake
    drawFlake2()

    # Wait for user
    wn.mainloop()

# Program Start
main()
