"""
Q49: File Handling Basics — Write and Read Text

Concepts:
- Write using w mode
- Append using a mode
- Read using r mode
- Compare open()/close() with the with statement
- Demonstrate all required file modes
- Show that w mode erases existing content
"""

from pathlib import Path

# Project data directory
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

STUDENT_FILE = DATA_DIR / "students.txt"

# 1. Write student data using w mode
with open(STUDENT_FILE, "w", encoding="utf-8") as file:
    file.write("Roll: 2626299\n")
    file.write("Name: Sona\n")
    file.write("Course: MCA\n")
    file.write("Python: 85\n")
    file.write("DBMS: 95\n")
    file.write("Statistics: 92\n")

print("1. Student data written using w mode.")

# 2. Append another student using a mode
with open(STUDENT_FILE, "a", encoding="utf-8") as file:
    file.write("\nRoll: 2626300\n")
    file.write("Name: Aman\n")
    file.write("Course: MCA\n")
    file.write("Python: 78\n")
    file.write("DBMS: 82\n")
    file.write("Statistics: 80\n")

print("2. Second student appended using a mode.")

# 3. Read using r mode
print("\n3. Reading student data using r mode:")
with open(STUDENT_FILE, "r", encoding="utf-8") as file:
    print(file.read())

# 4. Open and close manually
file = open(STUDENT_FILE, "r", encoding="utf-8")
content = file.read()
file.close()

print("4. Manual close successful:", file.closed)

# 5. Read using the with statement
with open(STUDENT_FILE, "r", encoding="utf-8") as file:
    content = file.read()

print("5. Automatic close successful:", file.closed)

# 6. Demonstrate w mode overwriting existing content
test_file = DATA_DIR / "w_mode_demo.txt"

with open(test_file, "w", encoding="utf-8") as file:
    file.write("OLD CONTENT\n")

with open(test_file, "w", encoding="utf-8") as file:
    file.write("NEW CONTENT\n")

with open(test_file, "r", encoding="utf-8") as file:
    print("\n6. Content after opening in w mode again:")
    print(file.read())

# 7. Demonstrate x mode safely with a separate test file
exclusive_file = DATA_DIR / "x_mode_demo.txt"

if exclusive_file.exists():
    exclusive_file.unlink()

with open(exclusive_file, "x", encoding="utf-8") as file:
    file.write("Created using x mode.\n")

print("7. File created using x mode.")

# 8. Demonstrate binary modes
binary_file = DATA_DIR / "binary_demo.bin"

with open(binary_file, "wb") as file:
    file.write(b"Hello Student")

with open(binary_file, "rb") as file:
    print("8. Binary content:", file.read())

print("\nAll Q49 demonstrations completed.")
