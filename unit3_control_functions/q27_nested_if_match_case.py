
"""
Q27: Nested if and match-case - Division Classification

This program calculates percentage, classifies the division
using nested if, and assigns a grade letter using match-case.
"""

# Read five subject marks
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

# Calculate total and percentage
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total_marks / 500) * 100

# Check if any subject is below 40
has_failed_subject = (
    mark1 < 40
    or mark2 < 40
    or mark3 < 40
    or mark4 < 40
    or mark5 < 40
)

# Division classification using nested if
if percentage >= 75:
    if not has_failed_subject:
        division = "Distinction"
    else:
        division = "First"
elif percentage >= 60:
    division = "First"
elif percentage >= 50:
    division = "Second"
elif percentage >= 40:
    division = "Third"
else:
    division = "Fail"

# Grade letter using match-case
if percentage >= 85:
    grade_code = "A"
elif percentage >= 70:
    grade_code = "B"
elif percentage >= 40:
    grade_code = "C"
else:
    grade_code = "F"

match grade_code:
    case "A":
        grade = "A"
    case "B":
        grade = "B"
    case "C":
        grade = "C"
    case "F":
        grade = "F"
    case _:
        grade = "Invalid"

# Display result
print(f"Total Marks: {total_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Division: {division}")
print(f"Grade: {grade}")
