
# Q15: Input and Type Conversion

# Read student details
name = input("Enter student name: ")
roll_no = input("Enter roll no: ")
age = int(input("Enter age: "))

# Read three subject marks as float
mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))

# Print values and their types
print("\nStudent Details:")
print("Name:", name, "Type:", type(name))
print("Roll No:", roll_no, "Type:", type(roll_no))
print("Age:", age, "Type:", type(age))
print("Mark 1:", mark1, "Type:", type(mark1))
print("Mark 2:", mark2, "Type:", type(mark2))
print("Mark 3:", mark3, "Type:", type(mark3))

# Without casting
# input() always returns a string.
# Example:
# age_text = input("Enter age: ")
# print(age_text + 1)
# This gives TypeError because str and int cannot be added.

print("\nType Conversion:")
age_text = input("Enter age again as text: ")

try:
    print(age_text + 1)
except TypeError:
    print("TypeError: Cannot add str and int.")

# Explicit conversion
age_number = int(age_text)
print("After int() conversion:", age_number + 1)
