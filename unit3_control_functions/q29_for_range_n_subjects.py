
"""
Q29: for loop and range() - N Subjects

This program asks for the number of subjects, reads each
subject name and mark using a for loop, and calculates
the total marks.

It also demonstrates different range() behaviours.
"""

# Ask for number of subjects
n = int(input("Enter number of subjects: "))

total_marks = 0

# Read subject names and marks using for loop
for i in range(n):
    print(f"\nSubject {i + 1}")
    subject_name = input("Enter subject name: ")
    mark = float(input("Enter marks: "))

    total_marks += mark

    print(f"{subject_name}: {mark:.2f}")

# Display total
print("\n===== RESULT =====")
print(f"Number of Subjects: {n}")
print(f"Total Marks: {total_marks:.2f}")

# Demonstrate range() behaviour
print("\n===== range() Behaviour =====")

print("range(5):", list(range(5)))
print("range(2,10):", list(range(2, 10)))
print("range(10,2,-2):", list(range(10, 2, -2)))
