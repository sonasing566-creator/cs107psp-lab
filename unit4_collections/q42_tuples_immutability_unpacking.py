"""
Q42: Tuples — Immutability and Unpacking

Demonstrates:
1. Creating tuples of subjects
2. Tuple immutability and TypeError
3. Single-element tuple
4. Tuple packing and unpacking
5. *rest unpacking
6. Function returning a tuple
7. count() and index()
8. Tuple to list and list to tuple conversion
9. Tuple as dictionary key
10. Why list cannot be a dictionary key
"""

print("===== SUBJECT TUPLES =====")

subjects = ("Python", "DBMS", "Statistics", "Cloud Computing")
print("Subjects tuple:", subjects)

print("\n===== TUPLE IMMUTABILITY =====")

try:
    subjects[0] = "Artificial Intelligence"
except TypeError as e:
    print("TypeError:", e)
    print("Tuples are immutable, so their elements cannot be changed.")

print("\n===== SINGLE-ELEMENT TUPLE =====")

single_tuple = (5,)
not_a_tuple = (5)

print("Single-element tuple:", single_tuple)
print("Type:", type(single_tuple))
print("Without comma:", not_a_tuple)
print("Type:", type(not_a_tuple))

print("\n===== TUPLE PACKING =====")

student = "Sona", 2626299, "MCA"
print("Packed tuple:", student)

print("\n===== TUPLE UNPACKING =====")

name, roll_number, course = student

print("Name:", name)
print("Roll Number:", roll_number)
print("Course:", course)

print("\n===== *REST UNPACKING =====")

marks = (85, 78, 92, 88, 90)

first, second, *rest = marks

print("First mark:", first)
print("Second mark:", second)
print("Rest of marks:", rest)

print("\n===== FUNCTION RETURNING A TUPLE =====")

def student_result():
    total = 433
    percentage = 86.6
    grade = "A"
    return total, percentage, grade


result = student_result()

print("Returned tuple:", result)

total, percentage, grade = student_result()

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)

print("\n===== COUNT() AND INDEX() =====")

subjects_with_duplicate = (
    "Python",
    "DBMS",
    "Python",
    "Statistics",
    "Python"
)

print("Subjects:", subjects_with_duplicate)
print("Count of Python:", subjects_with_duplicate.count("Python"))
print("Index of Statistics:", subjects_with_duplicate.index("Statistics"))

print("\n===== TUPLE TO LIST =====")

subject_list = list(subjects)
print("Tuple:", subjects)
print("Converted to list:", subject_list)

subject_list.append("AI")
print("List after append:", subject_list)

print("\n===== LIST TO TUPLE =====")

new_subjects = tuple(subject_list)
print("Converted back to tuple:", new_subjects)

print("\n===== TUPLE AS DICTIONARY KEY =====")

student_marks = {
    ("Sona", "Python"): 85,
    ("Sona", "DBMS"): 78,
    ("Riya", "Python"): 90
}

print("Dictionary:", student_marks)
print("Marks of Sona in Python:", student_marks[("Sona", "Python")])

print("\n===== WHY LIST CANNOT BE A DICTIONARY KEY =====")

try:
    invalid_dictionary = {
        ["Sona", "Python"]: 85
    }
except TypeError as e:
    print("TypeError:", e)
    print("A list cannot be used as a dictionary key because lists are mutable.")

print("\n===== Q42 COMPLETE =====")
