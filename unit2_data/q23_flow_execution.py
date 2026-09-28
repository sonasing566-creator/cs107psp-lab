
"""
Q23: Flow of Execution and Statement Order
"""

# Part A: Statement order
print("Start of program")

student_name = "Sona"
print("Student name:", student_name)

marks = 85
print("Marks:", marks)

print("After marks assignment")

percentage = marks / 300 * 100
print("Percentage:", round(percentage, 2))

print("End of program")


# Part B: Using a variable before it is defined
print("\nPart B: NameError demonstration")

try:
    print(undefined_variable)
except NameError as error:
    print("NameError:", error)

defined_variable = "Now the variable is defined"
print(defined_variable)


# Part C: Zen of Python
print("\nPart C: Zen of Python")
import this

print("\nThree Zen principles I will follow in this lab:")
print("1. Simple is better than complex.")
print("2. Readability counts.")
print("3. Errors should never pass silently.")


# Part D: Simple Interest using a multi-line expression
print("\nPart D: Simple Interest")

principal = 10000
rate = 5
time = 2

simple_interest = (
    principal
    * rate
    * time
    / 100
)

print("Simple Interest:", simple_interest)


# Part E: CGPA using a multi-line expression
print("\nPart E: CGPA")

grade_points = [8.5, 9.0, 8.0, 9.5, 8.5]

cgpa = (
    sum(grade_points)
    / len(grade_points)
)

print("CGPA:", cgpa)
