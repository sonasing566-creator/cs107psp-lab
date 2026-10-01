"""
Q43: Sets — Removing Duplicates and Comparing Groups

Demonstrates:
1. Sets of students who passed Maths
2. Sets of students who passed Physics
3. Union (|)
4. Intersection (&)
5. Difference (-)
6. Symmetric difference (^)
7. issubset()
8. add()
9. discard()
10. Removing duplicate subjects using set()
11. Why sets are unordered and unindexed
"""

print("===== CLASS MARKS =====")

class_marks = [
    ["Sona", 85, 78],
    ["Aman", 72, 81],
    ["Riya", 90, 95],
    ["Rahul", 35, 68],
    ["Neha", 80, 32],
    ["Priya", 65, 75]
]

print("Student marks:")
for student in class_marks:
    print(student)

print("\n===== STUDENTS WHO PASSED MATHS =====")

# Maths passing mark = 40
maths_passed = {
    student[0]
    for student in class_marks
    if student[1] >= 40
}

print("Maths passed:", maths_passed)

print("\n===== STUDENTS WHO PASSED PHYSICS =====")

# Physics passing mark = 40
physics_passed = {
    student[0]
    for student in class_marks
    if student[2] >= 40
}

print("Physics passed:", physics_passed)

print("\n===== SET UNION (|) =====")

both_or_any = maths_passed | physics_passed
print("Students who passed Maths OR Physics:", both_or_any)

print("\n===== SET INTERSECTION (&) =====")

both_subjects = maths_passed & physics_passed
print("Students who passed BOTH Maths AND Physics:", both_subjects)

print("\n===== SET DIFFERENCE (-) =====")

maths_only = maths_passed - physics_passed
physics_only = physics_passed - maths_passed

print("Passed Maths but not Physics:", maths_only)
print("Passed Physics but not Maths:", physics_only)

print("\n===== SYMMETRIC DIFFERENCE (^) =====")

different_subjects = maths_passed ^ physics_passed
print("Passed only one of the two subjects:", different_subjects)

print("\n===== issubset() =====")

passed_both_subset = both_subjects.issubset(maths_passed)

print(
    "Students who passed both are subset of Maths passed:",
    passed_both_subset
)

print("\n===== add() =====")

maths_passed.add("Vikram")
print("After adding Vikram:", maths_passed)

print("\n===== discard() =====")

maths_passed.discard("Vikram")
print("After discarding Vikram:", maths_passed)

# discard() does not give an error if the item is absent.
maths_passed.discard("Unknown")
print("After discarding Unknown:", maths_passed)

print("\n===== REMOVE DUPLICATE SUBJECT ENTRIES =====")

subjects = [
    "Python",
    "DBMS",
    "Python",
    "Statistics",
    "Cloud",
    "DBMS",
    "Python",
    "AI"
]

print("Original subjects:", subjects)

unique_subjects = set(subjects)

print("Unique subjects using set():", unique_subjects)

print("\n===== SETS ARE UNORDERED AND UNINDEXED =====")

print("A set does not maintain a fixed positional order.")
print("Therefore, indexing such as set_data[0] is not supported.")

try:
    print(unique_subjects[0])
except TypeError as e:
    print("TypeError:", e)
    print("Sets are unindexed, so elements cannot be accessed using [index].")

print("\n===== IMPORTANT POINTS =====")

print("1. Set stores unique elements.")
print("2. Duplicate values are automatically removed.")
print("3. Sets are unordered collections.")
print("4. Sets do not support indexing or slicing.")
print("5. | gives union.")
print("6. & gives intersection.")
print("7. - gives difference.")
print("8. ^ gives symmetric difference.")
print("9. issubset() checks whether one set is contained in another.")
print("10. add() adds an element and discard() removes an element safely.")

print("\n===== Q43 COMPLETE =====")
