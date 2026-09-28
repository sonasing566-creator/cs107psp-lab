
"""
Q22: Comments, Docstrings and PEP-8 Clean-Up.

This program demonstrates refactoring badly written code
into clean and readable Python code.
"""


# Badly written code example:
# n="Sona";a=21;m1=85;m2=78;m3=99;total=m1+m2+m3;per=total/300*100


def calculate_percentage(mark1, mark2, mark3):
    """
    Calculate the percentage from three subject marks.

    Returns:
        float: Percentage obtained by the student.
    """
    total_marks = mark1 + mark2 + mark3  # Calculate total marks
    percentage = total_marks / 300 * 100  # Calculate percentage

    # Line continuation using parentheses
    result = (
        f"Total Marks: {total_marks}, "
        f"Percentage: {percentage:.2f}%"
    )

    return result


def display_student_details(name, age, marks):
    """
    Display basic student information.

    Args:
        name (str): Student name.
        age (int): Student age.
        marks (list): List of subject marks.
    """
    print("Student Name:", name)
    print("Age:", age)
    print("Marks:", marks)

    # Line continuation using backslash
    message = "Student: " + name + \
              " | Age: " + str(age)

    print(message)


# Function call
student_name = "Sona Kumari"
student_age = 21
subject_marks = [85, 78, 99]

display_student_details(
    student_name,
    student_age,
    subject_marks
)

print(
    calculate_percentage(
        subject_marks[0],
        subject_marks[1],
        subject_marks[2]
    )
)

# Access function docstring using __doc__
print("\nFunction Docstring:")
print(calculate_percentage.__doc__)

# Access documentation using help()
print("\nHelp for calculate_percentage:")
help(calculate_percentage)
