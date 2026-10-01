"""
Q38: List Methods
Demonstrates common Python list methods.
"""

subjects = ["Python", "DBMS", "Statistics"]

print("===== ORIGINAL LIST =====")
print("Subjects:", subjects)

print("\n===== append() =====")
subjects.append("Cloud Computing")
print("After append:", subjects)

print("\n===== extend() =====")
subjects.extend(["AI", "Computer Networks"])
print("After extend:", subjects)

print("\n===== insert() =====")
subjects.insert(1, "Operating System")
print("After insert:", subjects)

print("\n===== remove() =====")
subjects.remove("Statistics")
print("After remove:", subjects)

print("\n===== pop() =====")
removed_subject = subjects.pop()
print("Popped subject:", removed_subject)
print("After pop:", subjects)

print("\n===== index() =====")
print("Index of DBMS:", subjects.index("DBMS"))

print("\n===== count() =====")
print("Count of Python:", subjects.count("Python"))

print("\n===== sort(reverse=) =====")
subjects.sort(reverse=True)
print("After sort(reverse=True):", subjects)

print("\n===== sorted() =====")
sorted_subjects = sorted(subjects)
print("Original list:", subjects)
print("New sorted list:", sorted_subjects)

print("\n===== reverse() =====")
subjects.reverse()
print("After reverse():", subjects)

print("\n===== clear() =====")
cleared_subjects = subjects.copy()
cleared_subjects.clear()
print("After clear():", cleared_subjects)

print("\n===== sort() vs sorted() =====")
print("sort() changes the original list.")
print("sorted() creates and returns a new sorted list.")

print("\n===== append() vs extend() =====")
print("append() adds one item as a single element.")
print("extend() adds each item from another iterable separately.")

print("\n===== Q38 COMPLETE =====")
