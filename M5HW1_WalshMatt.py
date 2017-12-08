# CTI 110
# M5HW1 Distance Traveled
# Matthew 'Melissa' Walsh
# 10.10.17
# This program calculates distance traveled using user given time and speed

def calcDistanceTraveled():
    speed = int(input("What is the speed of the vehicle in mph? "))

    time = int(input("How many hours did it travel? "))

    print("HOUR\t\t DISTANCE TRAVELLED")
    print("---------------------------------")

    a = 0
    while a < time:
        a = a + 1
        distance = speed * a
        print(a, "\t\t", distance)

def main():
    calcDistanceTraveled()

# Program Start

main()
