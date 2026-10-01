"""
Q41: List Comprehension and Advanced List Processing

Demonstrates:
1. Percentages using list comprehension
2. Toppers using comprehension with if
3. Grade letters using conditional expression
4. Flattening a nested list
5. Building a 3x3 matrix using nested comprehension
6. Readability comparison
7. Timing comparison using time.perf_counter()
"""

import time


class_marks = [
    ["Sona", 85, 78, 92, 88, 90],
    ["Aman", 72, 81, 75, 80, 77],
    ["Riya", 90, 95, 88, 92, 94],
    ["Rahul", 65, 70, 68, 72, 66],
    ["Neha", 80, 85, 82, 78, 84]
]


print("===== ORIGINAL CLASS MARKS =====")
for row in class_marks:
    print(row)


print("\n===== PERCENTAGES USING COMPREHENSION =====")

percentages = [sum(r[1:]) / 5 for r in class_marks]

for i in range(len(class_marks)):
    print(class_marks[i][0], "Percentage:", round(percentages[i], 2))


print("\n===== TOPPERS USING COMPREHENSION WITH IF =====")

toppers = [
    class_marks[i][0]
    for i in range(len(class_marks))
    if percentages[i] >= 85
]

print("Toppers (>= 85%):", toppers)


print("\n===== GRADE LETTERS USING CONDITIONAL EXPRESSION =====")

grades = [
    "A" if percentage >= 85
    else "B" if percentage >= 70
    else "C" if percentage >= 50
    else "D"
    for percentage in percentages
]

for i in range(len(class_marks)):
    print(class_marks[i][0], "->", grades[i])


print("\n===== FLATTEN NESTED LIST =====")

nested_marks = [
    [85, 78, 92],
    [72, 81, 75],
    [90, 95, 88]
]

flattened = [mark for row in nested_marks for mark in row]

print("Nested list:", nested_marks)
print("Flattened list:", flattened)


print("\n===== 3x3 MATRIX USING NESTED COMPREHENSION =====")

matrix = [
    [row * 3 + column + 1 for column in range(3)]
    for row in range(3)
]

for row in matrix:
    print(row)


print("\n===== LOOP VERSION: PERCENTAGES =====")

loop_percentages = []

for row in class_marks:
    total = sum(row[1:])
    percentage = total / 5
    loop_percentages.append(percentage)

print("Loop percentages:", [round(p, 2) for p in loop_percentages])


print("\n===== COMPREHENSION VERSION: PERCENTAGES =====")

comprehension_percentages = [
    sum(row[1:]) / 5
    for row in class_marks
]

print(
    "Comprehension percentages:",
    [round(p, 2) for p in comprehension_percentages]
)


print("\n===== READABILITY COMPARISON =====")

print("Loop version: longer but easier for beginners and complex logic.")
print("Comprehension: shorter and convenient for simple transformations.")
print("For complex logic, normal loops can be more readable.")


print("\n===== TIMING COMPARISON =====")

iterations = 100000

start = time.perf_counter()

for _ in range(iterations):
    loop_result = []
    for row in class_marks:
        loop_result.append(sum(row[1:]) / 5)

loop_time = time.perf_counter() - start


start = time.perf_counter()

for _ in range(iterations):
    comprehension_result = [
        sum(row[1:]) / 5
        for row in class_marks
    ]

comprehension_time = time.perf_counter() - start


print("Iterations:", iterations)
print("Loop time:", loop_time, "seconds")
print("Comprehension time:", comprehension_time, "seconds")

if comprehension_time < loop_time:
    print("Timing result: comprehension was faster in this run.")
elif loop_time < comprehension_time:
    print("Timing result: loop was faster in this run.")
else:
    print("Timing result: both took approximately the same time.")


print("\n===== Q41 COMPLETE =====")
