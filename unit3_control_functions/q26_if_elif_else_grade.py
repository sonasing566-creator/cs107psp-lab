
"""
Q26: if-elif-else - Grade Assignment

This program assigns a grade based on percentage.
"""

percentage = float(input("Enter percentage: "))

if percentage >= 85:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 40:
    grade = "C"
elif percentage >= 0:
    grade = "D"
else:
    grade = "F"

print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
