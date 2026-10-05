"""
Q45: Dictionary Methods and Comprehension
"""

print("===== ORIGINAL DICTIONARY =====")

student = {
    "roll": "22CSE001",
    "name": "Asha",
    "marks": 88
}

print("Student:", student)

print("\n===== keys() =====")
print("Keys:", student.keys())

print("\n===== values() =====")
print("Values:", student.values())

print("\n===== items() =====")
print("Items:", student.items())

print("\n===== get() =====")
print("Name using get():", student.get("name"))
print("Address using get():", student.get("address"))
print("City using get() with default:", student.get("city", "Not Available"))

print("\n===== setdefault() =====")

student.setdefault("course", "MCA")
print("After setdefault('course', 'MCA'):", student)

student.setdefault("name", "Changed Name")
print("After setdefault() on existing name:", student)

print("\n===== update() =====")

student.update({
    "semester": 1,
    "marks": 90
})

print("After update():", student)

print("\n===== fromkeys() =====")

subjects = ["Python", "DBMS", "Statistics", "Cloud"]
default_marks = dict.fromkeys(subjects, 0)

print("Subjects:", subjects)
print("Dictionary using fromkeys():", default_marks)

print("\n===== copy() =====")

student_copy = student.copy()

print("Original dictionary:", student)
print("Copied dictionary:", student_copy)

student_copy["name"] = "Riya"

print("After changing copied dictionary:")
print("Original:", student)
print("Copy:", student_copy)

print("\n===== ITERATING USING items() =====")

for k, v in student.items():
    print("Key:", k, "| Value:", v)

print("\n===== DICT COMPREHENSION USING zip() =====")

subject_names = ["Python", "DBMS", "Statistics", "Cloud", "AI"]
marks = [85, 78, 92, 88, 90]

subject_marks = {
    subject: mark
    for subject, mark in zip(subject_names, marks)
}

print("Subjects:", subject_names)
print("Marks:", marks)
print("Subject-Marks dictionary:", subject_marks)

print("\n===== INVERT DICTIONARY USING COMPREHENSION =====")

original = {
    "Python": 85,
    "DBMS": 78,
    "Statistics": 92
}

inverted = {
    mark: subject
    for subject, mark in original.items()
}

print("Original dictionary:", original)
print("Inverted dictionary:", inverted)

print("\n===== IMPORTANT POINTS =====")

print("1. keys() returns dictionary keys.")
print("2. values() returns dictionary values.")
print("3. items() returns key-value pairs.")
print("4. get() safely accesses a key.")
print("5. setdefault() adds a key only if it does not already exist.")
print("6. update() adds or changes key-value pairs.")
print("7. fromkeys() creates a dictionary from given keys.")
print("8. copy() creates a shallow copy of the dictionary.")
print("9. zip() combines two lists element by element.")
print("10. Dictionary comprehension creates dictionaries in a short form.")

print("\n===== Q45 COMPLETE =====")
