# CTI 110
# M5T2 Bug Collector
# Matthew 'Melissa' Walsh
# 10.05.17
# This program uses loops to calculate how many bugs a person collected
# over a certain number of days

# For Loop Method
def bugCountFor():

    # Initalize variables
    total = 0

    # Get the bugs collected for each day
    for day in range(1, 8):
        print('Enter the bugs collected on day', day)
        bugs = int(input())
        total += bugs

    # Display total bugs
    print("You collected a total of", total, "bugs.")

# While Loop Method
def bugCountWhile():

    # Initalize variables
    i = 0
    total = 0

    # Prompt user for number of days
    days = int(input("How many days would you like to collect bugs for?: "))

    # Get bugs collected for each day
    while i < days:
        i = i + 1
        
        print('Enter the bugs collected on day', i)
        bugs = int(input())
        total += bugs

    # Display total bugs
    print("You collected a total of", total, "bugs.")

# Main Method
def main():

    print("This method uses a for loop!")
    bugCountFor()
    
    print("\nThis method uses a while loop!")
    bugCountWhile()


# Program Start

main()
