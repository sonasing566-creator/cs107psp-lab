"""
Q53: Math Utilities Module

Functions:
1. average()     - calculates the average
2. percentage()  - calculates the percentage
3. grade()       - returns a grade based on marks
"""


def average(numbers):
    """Return the average of a list of numbers."""
    if not numbers:
        raise ValueError("The list cannot be empty.")
    return sum(numbers) / len(numbers)


def percentage(obtained, total):
    """Calculate percentage from obtained and total marks."""
    if total <= 0:
        raise ValueError("Total marks must be greater than zero.")
    if obtained < 0 or obtained > total:
        raise ValueError("Obtained marks must be between 0 and total.")
    return (obtained / total) * 100


def grade(mark):
    """Return a grade based on marks out of 100."""
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")

    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"


# This block runs only when mathutils.py is executed directly.
if __name__ == "__main__":
    print("mathutils.py is running directly.")
    print("Average:", average([80, 90, 70]))
    print("Percentage:", percentage(85, 100))
    print("Grade:", grade(85))
