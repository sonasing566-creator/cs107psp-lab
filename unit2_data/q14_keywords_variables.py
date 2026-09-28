
# Q14: Variables, Keywords and Naming Rules

import keyword

# (a) Print all Python keywords
print("Python Keywords:")
print(keyword.kwlist)


# (b) 5 valid identifiers
print("\n5 Valid Identifiers:")
student_name = "Sona"
student_age = 22
total_marks = 85
course1 = "MCA"
_roll_no = 2626299

print(student_name)
print(student_age)
print(total_marks)
print(course1)
print(_roll_no)


# 5 invalid identifiers
# 1student = "Sona"       # Invalid: cannot start with a number
# student-name = "Sona"   # Invalid: hyphen is not allowed
# student name = "Sona"   # Invalid: spaces are not allowed
# class = "MCA"            # Invalid: 'class' is a Python keyword
# @student = "Sona"        # Invalid: special character @ is not allowed


# (c) Multiple assignment
a, b, c = 1, 2, 3
print("\nMultiple Assignment:")
print("a =", a)
print("b =", b)
print("c =", c)


# (d) Swap two variables in one line
x = 10
y = 20

print("\nBefore Swap:")
print("x =", x)
print("y =", y)

x, y = y, x

print("After Swap:")
print("x =", x)
print("y =", y)


# (e) del statement
student = "Sona"
print("\nBefore del:", student)

del student

print("Variable 'student' has been deleted.")
