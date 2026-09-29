"""
Q25: if and if-else - Pass or Fail

This program reads a student's name, roll number, and five subject marks.
It calculates total and percentage and uses if-else to decide PASS or FAIL.

If any mark is negative, the student is marked as Absent.
"""

# Read student details
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

# Read five subject marks
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

# Calculate total and percentage
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total_marks / 500) * 100

# Check whether any mark is negative
if (
    mark1 < 0
    or mark2 < 0
    or mark3 < 0
    or mark4 < 0
    or mark5 < 0
):
    print("Absent")
else:
    # Decide PASS or FAIL
    if percentage >= 40:
        print("PASS")
    else:
        print("FAIL")

# Display student result
print(f"Student Name: {student_name}")
print(f"Roll Number: {roll_number}")
print(f"Total Marks: {total_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
