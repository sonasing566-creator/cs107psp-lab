"""
Q32: Functions - def, call, parameters and return

This program converts the Q26 grade logic into functions.
It also demonstrates a function with no return value.
"""


def calc_total(marks):
    """Calculate total marks."""
    return sum(marks)


def calc_percentage(total, count):
    """Calculate percentage from total marks and subject count."""
    return (total / (count * 100)) * 100


def assign_grade(pct):
    """Assign grade according to percentage."""
    if pct >= 85:
        return "A"
    elif pct >= 70:
        return "B"
    elif pct >= 40:
        return "C"
    elif pct >= 0:
        return "D"
    else:
        return "F"


def print_marksheet(name, roll, marks):
    """Print the student's mark sheet."""
    total = calc_total(marks)
    percentage = calc_percentage(total, len(marks))
    grade = assign_grade(percentage)

    print("\n===== MARK SHEET =====")
    print(f"Student Name: {name}")
    print(f"Roll Number: {roll}")

    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i}: {mark:.2f}")

    print(f"Total Marks: {total:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


def show_message():
    """Function with no return statement."""
    print("This function does not return a value.")


def main():
    """Main function."""
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    count = int(input("Enter number of subjects: "))

    marks = []

    for i in range(count):
        mark = float(input(f"Enter marks for Subject {i + 1}: "))
        marks.append(mark)

    print_marksheet(name, roll, marks)

    result = show_message()
    print(f"Return value of show_message(): {result}")


if __name__ == "__main__":
    main()
