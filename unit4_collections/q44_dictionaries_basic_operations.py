"""
Q44: Dictionaries — Creation and Basic Operations

Demonstrates:
1. Dictionary creation
2. Accessing values using []
3. Adding a new key
4. Updating an existing key
5. Deleting a key using del
6. Removing a key using pop()
7. Removing the last inserted item using popitem()
8. KeyError demonstration
9. get() to safely access a missing key
"""

print("===== DICTIONARY CREATION =====")

student = {
    "roll": "22CSE001",
    "name": "Asha",
    "marks": [78, 92, 45, 66, 88]
}

print("Student dictionary:", student)

print("\n===== ACCESSING VALUES USING [] =====")

print("Roll:", student["roll"])
print("Name:", student["name"])
print("Marks:", student["marks"])

print("\n===== ADDING A NEW KEY =====")

student["course"] = "MCA"

print("After adding course:", student)

print("\n===== UPDATING AN EXISTING KEY =====")

student["name"] = "Asha Sharma"

print("Updated name:", student["name"])
print("Updated dictionary:", student)

print("\n===== ADDING ANOTHER KEY =====")

student["semester"] = 1

print("After adding semester:", student)

print("\n===== DELETE USING del =====")

del student["semester"]

print("After del semester:", student)

print("\n===== DELETE USING pop() =====")

removed_course = student.pop("course")

print("Removed value:", removed_course)
print("After pop('course'):", student)

print("\n===== DELETE USING popitem() =====")

removed_item = student.popitem()

print("Removed item:", removed_item)
print("After popitem():", student)

print("\n===== KEYERROR USING [] =====")

try:
    print(student["address"])
except KeyError as e:
    print("KeyError:", e)
    print("The key 'address' does not exist in the dictionary.")

print("\n===== get() AVOIDS KEYERROR =====")

address = student.get("address")

print("student.get('address'):", address)

if address is None:
    print("Address key does not exist, but no KeyError occurred.")

print("\n===== get() WITH DEFAULT VALUE =====")

city = student.get("city", "Not Available")

print("City:", city)

print("\n===== FINAL DICTIONARY =====")

print(student)

print("\n===== IMPORTANT POINTS =====")

print("1. [] directly accesses a dictionary value.")
print("2. [] raises KeyError if the key does not exist.")
print("3. get() safely accesses a key and returns None or a default value.")
print("4. del removes a specified key.")
print("5. pop() removes a specified key and returns its value.")
print("6. popitem() removes and returns the last inserted key-value pair.")

print("\n===== Q44 COMPLETE =====")
