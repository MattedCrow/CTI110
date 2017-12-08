# CTI 110
# M6HW1 - Test Grading Program
# Matthew 'Melissa' Walsh
# 11.16.17
# This program calculates user entered grades and averages.

# Calculate Average
def calc_average(score1, score2, score3, score4, score5):
    total = score1 + score2 + score3 + score4 + score5

    average = total / 5

    return average

# Determine Grade
def determine_grade(score):
    # Grading Scale
    A_SCORE = 90
    B_SCORE = 80
    C_SCORE = 70
    D_SCORE = 60

    if score >= A_SCORE:
        grade = "A"
    elif score >= B_SCORE:
        grade = "B"
    elif score >= C_SCORE:
        grade = "C"
    elif score >= D_SCORE:
        grade = "D"
    elif score < 0:
        grade = "F"
    else:
        grade = "F"

    return grade

# Main Method
def main():
    score1 = float(input("Enter Score 1: "))
    grade1 = determine_grade(score1)

    score2 = float(input("Enter Score 2: "))
    grade2 = determine_grade(score2)

    score3 = float(input("Enter Score 3: "))
    grade3 = determine_grade(score3)

    score4 = float(input("Enter Score 4: "))
    grade4 = determine_grade(score4)

    score5 = float(input("Enter Score 5: "))
    grade5 = determine_grade(score5)

    average = calc_average(score1, score2, score3, score4, score5)
    averageGrade = determine_grade(average)

    # Print Output
    print("Score\t\t\tNumeric Grade\tLetter Grade")
    print("-------------------------------------------------------------------")
    print("Score 1:\t\t", score1, "\t\t", grade1)
    print("Score 2:\t\t", score2, "\t\t", grade2)
    print("Score 3:\t\t", score3, "\t\t", grade3)
    print("Score 4:\t\t", score4, "\t\t", grade4)
    print("Score 5:\t\t", score5, "\t\t", grade5)
    print("-------------------------------------------------------------------")
    print("Average:\t\t", average, "\t\t", averageGrade)

# Run Main Method
main()

    
