# CTI 110
# M6T1 - Kilometer Converter
# Matthew 'Melissa' Walsh
# 11.14.17
# This program converts kilometers to miles

CONVERSION_FACTOR = 0.6214

# To Miles
def toMiles():
    # Get the distance in kilometers
    try:
        kilometers = float(input('Enter a distance in kilometers: '))

        validation = isValid(kilometers)

        if validation == "true":
            # Display the distance converted to miles
            show_miles(kilometers)
        else:
            print("Invalid input, please enter a positive number.")
            toMiles()
    except:
        print("Invalid input, please enter a positive number.")
        toMiles()

# To Kilometers
def toKilo():
    # Get the distance in kilometers
    try:
        miles = float(input('Enter a distance in miles: '))

        validation = isValid(miles)

        if validation == "true":
            # Display the distance converted to miles
            show_kilos(miles)
        else:
            print("Invalid input, please enter a positive number.")
            toKilo()
    except:
        print("Invalid input, please enter a positive number.")
        toKilo()

# Show Miles Method
def show_miles(km):
    # Calculate miles
    miles = km * CONVERSION_FACTOR

    # Display the miles
    print(km, 'kilometers equals', miles, 'miles.')

# Show Kilometers Method
def show_kilos(mi):
    # Calculate kilometers
    km = mi / CONVERSION_FACTOR

    # Display the kilometers
    print(mi, 'miles equals', km, 'kilometers.')

# Valid Number Method
def isValid(num):
    # Check it's positive
    if num > 0:
        validator = "true"
        return validator
    else:
        validator = "false"
        return validator

# Main Method
def main():
    choice = input("Would you like to convert 'to' or 'from' kilometers? ")

    valid = "false"
    
    while valid == "false":
        choice = choice.lower()
        if choice == "to":
            valid = "true"
        elif choice == "from":
            valid = "true"
        else:
            choice = input("Invalid input, please enter either 'to' or 'from'. ")

    if choice == "to":
        toKilo()
    elif choice == "from":
        toMiles()
    else:
        print("How did you manage this???")

# Run Main method
main()
