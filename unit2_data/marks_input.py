"""
Q24: Unit-2 Consolidation - Student Mark Sheet

This program reads a student's name, roll number, and five subject marks.
It calculates the total and percentage and displays a formatted mark sheet.

Note:
No if statements or loops are used because decision-making and repetition
will be introduced in Unit 3.
"""

# Read student details
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

# Read five subject marks and convert them to float
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

# Calculate total marks
total_marks = mark1 + mark2 + mark3 + mark4 + mark5

# Calculate percentage
percentage = (total_marks / 500) * 100

# Display the mark sheet
print("\n+" + "-" * 50 + "+")
print("|" + "VIDYA ANALYTICS".center(50) + "|")
print("|" + "STUDENT MARK SHEET".center(50) + "|")
print("+" + "-" * 50 + "+")

print(f"| {'Student Name':<20}: {student_name:<25}|")
print(f"| {'Roll Number':<20}: {roll_number:<25}|")

print("+" + "-" * 50 + "+")

print(f"| {'Subject 1':<20}: {mark1:>25.2f} |")
print(f"| {'Subject 2':<20}: {mark2:>25.2f} |")
print(f"| {'Subject 3':<20}: {mark3:>25.2f} |")
print(f"| {'Subject 4':<20}: {mark4:>25.2f} |")
print(f"| {'Subject 5':<20}: {mark5:>25.2f} |")

print("+" + "-" * 50 + "+")

print(f"| {'Total Marks':<20}: {total_marks:>25.2f} |")
print(f"| {'Percentage':<20}: {percentage:>24.2f}% |")

print("+" + "-" * 50 + "+")
