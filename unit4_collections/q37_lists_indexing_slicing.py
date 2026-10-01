"""
Q37: Lists — Creation, Indexing and Slicing
"""

# Create a list of marks
marks = [78, 92, 45, 66, 88]

print("===== LIST CREATION =====")
print("Marks:", marks)

print("\n===== POSITIVE INDEXING =====")
print("marks[0]:", marks[0])
print("marks[1]:", marks[1])
print("marks[2]:", marks[2])
print("marks[3]:", marks[3])
print("marks[4]:", marks[4])

print("\n===== NEGATIVE INDEXING =====")
print("marks[-1]:", marks[-1])
print("marks[-2]:", marks[-2])
print("marks[-3]:", marks[-3])
print("marks[-4]:", marks[-4])
print("marks[-5]:", marks[-5])

print("\n===== LIST SLICING =====")
print("marks[1:4]:", marks[1:4])
print("marks[:3]:", marks[:3])
print("marks[::2]:", marks[::2])
print("marks[::-1]:", marks[::-1])

print("\n===== SLICE ASSIGNMENT =====")
updated_marks = marks.copy()
print("Before:", updated_marks)
updated_marks[1:3] = [95, 85]
print("After marks[1:3] = [95, 85]:", updated_marks)

print("\n===== LIST BUILT-IN FUNCTIONS =====")
print("len(marks):", len(marks))
print("max(marks):", max(marks))
print("min(marks):", min(marks))
print("sum(marks):", sum(marks))

    
print("\n===== INDEX ERROR DEMONSTRATION =====")

try:
    print("marks[5]:", marks[5])
except IndexError as error:
    print("IndexError:", error)
    print("Explanation: Index 5 does not exist because the valid indexes are 0 to 4.")
