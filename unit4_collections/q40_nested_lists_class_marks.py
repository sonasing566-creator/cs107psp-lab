"""
Q40: Nested Lists — Class Marks Matrix

Demonstrates:
1. Nested lists
2. Row-wise student totals
3. Column-wise subject averages
4. Class topper
5. Toughest subject
"""

class_marks = [
    ["Sona", 85, 78, 92, 88, 90],
    ["Aman", 72, 81, 75, 80, 77],
    ["Riya", 90, 95, 88, 92, 94],
    ["Rahul", 65, 70, 68, 72, 66],
    ["Neha", 80, 85, 82, 78, 84]
]

subjects = ["Python", "DBMS", "Statistics", "Cloud", "AI"]

print("===== CLASS MARKS MATRIX =====")
for student in class_marks:
    print(student)


print("\n===== ROW-WISE STUDENT TOTALS =====")

student_totals = []

for student in class_marks:
    name = student[0]
    marks = student[1:]
    total = sum(marks)
    student_totals.append([name, total])
    print(name, "Total:", total)


print("\n===== COLUMN-WISE SUBJECT AVERAGES =====")

subject_averages = []

for column in range(1, 6):
    total = 0

    for student in class_marks:
        total += student[column]

    average = total / len(class_marks)
    subject_averages.append(average)

    print(subjects[column - 1], "Average:", round(average, 2))


print("\n===== CLASS TOPPER =====")

topper = max(student_totals, key=lambda student: student[1])

print("Topper:", topper[0])
print("Topper Total:", topper[1])


print("\n===== TOUGHEST SUBJECT =====")

# The subject with the lowest average is considered toughest.
toughest_index = subject_averages.index(min(subject_averages))
toughest_subject = subjects[toughest_index]

print("Toughest Subject:", toughest_subject)
print("Lowest Average:", round(subject_averages[toughest_index], 2))


print("\n===== SUMMARY =====")
print("Number of students:", len(class_marks))
print("Number of subjects:", len(subjects))

print("\nStudent Totals:")
for item in student_totals:
    print(item[0], "->", item[1])

print("\nSubject Averages:")
for i in range(len(subjects)):
    print(subjects[i], "->", round(subject_averages[i], 2))

print("\n===== Q40 COMPLETE =====")
