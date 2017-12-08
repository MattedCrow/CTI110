# CTI 110
# M6T2 - Feet to Inches
# Matthew 'Melissa' Walsh
# 11.14.17
# This program converts feet to inches

INCHES_PER_FOOT = 12;

# Calculate number of inches in the foot
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT;

# Valid Number Method
def isValid(num):
    # Check it's positive
    if num > 0:
        validator = "true"
        return validator
    else:
        validator = "false"
        return validator

# main function
def main():
    try:
        # Get the number of feet
        feet = float(input("Please entered the desire number of feet: "))

        if isValid(feet) == "true":
            # Display the distance converted to feet
            print("\t", feet, 'feet equals', feet_to_inches(feet), 'inches.')
        else:
            print("\tPlease enter a positive number.")
            main()
    except:
        print("\tInvalid input, please be sure to enter a positive number.")
        main()

# Run Main method
main()
