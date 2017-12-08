# CTI 110
# M6T2 - Feet to Inches
# Matthew 'Melissa' Walsh
# 11.16.17
# This program converts feet to inches

INCHES_PER_FOOT = 12;

# Calculate number of inches in the foot
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT;

# main function
def main():
    # Get the number of feet
    feet = float(input("Please entered the desire number of feet: "))

    # Send to method to convert to inches
    inches = feet_to_inches(feet)

    # Print results
    print(feet, "feet is equal to", inches, "inches.")

# Run Main method
main()
