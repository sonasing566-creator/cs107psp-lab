"""
Q31: Nested Loops - Tables and Patterns

This program demonstrates:
(a) Subject x Student marks grid
(b) Multiplication tables 1-10
(c) Star patterns and Floyd's triangle
"""

# Part (a): Subject x Student marks grid
print("===== SUBJECT x STUDENT MARKS GRID =====")

subjects = ["Python", "DBMS", "Statistics"]
students = ["Sona", "Riya", "Aman"]

marks = [
    [85, 90, 78],
    [88, 76, 92],
    [80, 84, 75]
]

print(f"{'Subject':<15}", end="")
for student in students:
    print(f"{student:<10}", end="")
print()

for i in range(len(subjects)):
    print(f"{subjects[i]:<15}", end="")
    for j in range(len(students)):
        print(f"{marks[i][j]:<10}", end="")
    print()


# Part (b): Multiplication table 1-10
print("\n===== MULTIPLICATION TABLE 1-10 =====")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()


# Part (c): Patterns
n = int(input("\nEnter number of rows for patterns: "))

# Right triangle
print("\n===== RIGHT TRIANGLE =====")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Inverted triangle
print("\n===== INVERTED TRIANGLE =====")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pyramid
print("\n===== PYRAMID =====")
for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

# Floyd's triangle
print("\n===== FLOYD'S TRIANGLE =====")
number = 1

for i in range(1, n + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()
