"""Grading functions for VIDYA Analytics."""


def calculate_percentage(obtained, total):
    """Calculate percentage from obtained and total marks."""
    if total <= 0:
        raise ValueError("Total marks must be greater than zero.")
    if obtained < 0 or obtained > total:
        raise ValueError("Obtained marks must be between 0 and total.")
    return (obtained / total) * 100


def assign_grade(percentage):
    """Assign a grade based on percentage."""
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100.")

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def is_pass(percentage):
    """Return True if percentage is at least 40."""
    return percentage >= 40
