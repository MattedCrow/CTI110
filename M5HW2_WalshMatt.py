# CTI 110
# M5HW2 Running Total
# Matthew 'Melissa' Walsh
# 10.10.17
# This program calculates a running total based on user entered numbers

def runningTotal():
    num = 0

    total = 0

    while num >= 0:
        total = total + num
        num = int(input("Please enter a number: "))

    print("\tTotal: ", total)

def main():
    print("This program will calculate a running total. To finish, enter a negative number.\n")

    runningTotal()

# Program Start
main()
