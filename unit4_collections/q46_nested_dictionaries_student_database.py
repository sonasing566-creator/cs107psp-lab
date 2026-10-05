"""
Q46: Nested Dictionaries — The Student Database
"""

print("===== NESTED DICTIONARY: STUDENT DATABASE =====")

students = {
    "S001": {
        "name": "Sona",
        "course": "MCA",
        "semester": 1,
        "marks": {
            "Python": 85,
            "DBMS": 78,
            "Statistics": 92
        }
    },
    "S002": {
        "name": "Aman",
        "course": "MCA",
        "semester": 1,
        "marks": {
            "Python": 72,
            "DBMS": 81,
            "Statistics": 75
        }
    },
    "S003": {
        "name": "Riya",
        "course": "MCA",
        "semester": 1,
        "marks": {
            "Python": 90,
            "DBMS": 95,
            "Statistics": 88
        }
    }
}

print("\n===== COMPLETE DATABASE =====")
print(students)

print("\n===== ACCESSING STUDENT =====")
print("S001:", students["S001"])

print("\n===== ACCESSING NESTED VALUES =====")
print("Name:", students["S001"]["name"])
print("Course:", students["S001"]["course"])
print("Python Marks:", students["S001"]["marks"]["Python"])

print("\n===== ADDING A NEW STUDENT =====")

students["S004"] = {
    "name": "Rahul",
    "course": "MCA",
    "semester": 1,
    "marks": {
        "Python": 65,
        "DBMS": 70,
        "Statistics": 68
    }
}

print("After adding S004:")
print(students["S004"])

print("\n===== UPDATING MARKS =====")

students["S001"]["marks"]["Python"] = 90

print("Updated Sona's Python marks:",
      students["S001"]["marks"]["Python"])

print("\n===== ITERATING THROUGH DATABASE =====")

for roll, details in students.items():
    print("Roll:", roll)
    print("Name:", details["name"])
    print("Course:", details["course"])
    print("Semester:", details["semester"])
    print("Marks:", details["marks"])
    print()

print("===== Q46 COMPLETE =====")
