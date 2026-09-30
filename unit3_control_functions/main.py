"""
Q36: UNIT-3 CONSOLIDATION
String Methods, Arrays and gradelib.py
"""

from array import array

from gradelib import (
    calculate_total,
    calculate_average,
    calculate_grade,
    create_marksheet,
    analyse,
    factorial,
    fibonacci_recursive,
    sum_digits,
    reverse_string,
    gcd_recursive
)


# ==========================================
# PART 1 — Grading Engine from gradelib.py
# ==========================================

name = "Sona Kumari"
roll_number = "2626299"
marks = [85, 78, 92, 88, 90]

print("===== VIDYA ANALYTICS =====")
print("Student:", name)
print("Roll Number:", roll_number)
print("Marks:", marks)

total = calculate_total(marks)
average = calculate_average(marks)
grade = calculate_grade(average)

print("\n===== MARKSHEET =====")
print("Total:", total)
print("Average:", average)
print("Grade:", grade)

print("\n===== ANALYSIS =====")
print("Analysis:", analyse(marks))

print("\n===== RECURSION FUNCTIONS =====")
print("Factorial(5):", factorial(5))
print("Fibonacci(10):", fibonacci_recursive(10))
print("Sum of roll-number digits:", sum_digits(int(roll_number)))
print("Reverse of VIDYA:", reverse_string("VIDYA"))
print("GCD(48, 18):", gcd_recursive(48, 18))

print("\n===== COMPLETE MARKSHEET =====")
print(create_marksheet(name, roll_number, marks))


# ==========================================
# PART 2 — String Methods
# ==========================================

print("\n===== STRING METHODS =====")

raw_name = "   sona kumari   "

print("Original:", repr(raw_name))
print("strip():", raw_name.strip())

clean_name = raw_name.strip()

print("title():", clean_name.title())
print("upper():", clean_name.upper())
print("lower():", clean_name.lower())
print("replace():", clean_name.replace("sona", "Sona"))

words = clean_name.split()
print("split():", words)

print("join():", "-".join(words))
print("find('kumari'):", clean_name.find("kumari"))
print("count('a'):", clean_name.count("a"))
print("startswith('sona'):", clean_name.startswith("sona"))
print("isalpha('Sona'):", "Sona".isalpha())
print("isdigit('2626299'):", "2626299".isdigit())


# ==========================================
# PART 3 — Roll Number Validation
# ==========================================

print("\n===== ROLL NUMBER VALIDATION =====")

roll = "22CSE001"

year = roll[:2]
branch = roll[2:5]
number = roll[5:]

valid_roll = (
    len(roll) == 8
    and year.isdigit()
    and branch.isalpha()
    and branch.isupper()
    and number.isdigit()
)

print("Roll Number:", roll)
print("Year:", year)
print("Branch:", branch)
print("Number:", number)
print("Valid Roll Number:", valid_roll)


# ==========================================
# PART 4 — Array
# ==========================================

print("\n===== ARRAY DEMONSTRATION =====")

marks_array = array("i", [85, 78, 92, 88, 90])

print("Original array:", marks_array)
print("Array type:", type(marks_array))

marks_array.append(95)
print("After append(95):", marks_array)

marks_array.insert(1, 80)
print("After insert(1, 80):", marks_array)

marks_array.remove(92)
print("After remove(92):", marks_array)

print("buffer_info():", marks_array.buffer_info())


# ==========================================
# PART 5 — Array vs List
# ==========================================

print("\n===== ARRAY VS LIST =====")

print("1. Array stores elements of the same data type; a list can store different data types.")
print("2. Array is generally more memory-efficient for large numeric data; lists use more memory.")
print("3. Array requires a type code such as 'i'; list does not require a type code.")


print("\n===== Q36 COMPLETE =====")
