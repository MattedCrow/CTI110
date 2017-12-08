# CTI 110
# M6T1 - Kilometer Converter
# Matthew 'Melissa' Walsh
# 11.14.17
# This program converts kilometers to miles

CONVERSION_FACTOR = 0.6214

# To Miles
def toMiles():
    # Get the distance in kilometers
    kilometers = float(input('Enter a distance in kilometers: '))

    show_miles(kilometers)

# Show Miles Method
def show_miles(km):
    # Calculate miles
    miles = km * CONVERSION_FACTOR

    # Display the miles
    print(km, 'kilometers equals', miles, 'miles.')

# Main Method
def main():
    toMiles()

# Run Main method
main()
