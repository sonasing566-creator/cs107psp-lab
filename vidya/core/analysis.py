"""Analysis functions for VIDYA Analytics."""

from statistics import mean, median, stdev


def analyse_marks(marks):
    """Return summary statistics for a list of marks."""
    if not marks:
        raise ValueError("Marks list cannot be empty.")

    result = {
        "count": len(marks),
        "average": mean(marks),
        "median": median(marks),
        "highest": max(marks),
        "lowest": min(marks),
    }

    if len(marks) > 1:
        result["standard_deviation"] = stdev(marks)
    else:
        result["standard_deviation"] = 0.0

    return result


def rank_students(students):
    """Rank students by their 'marks' value, highest first."""
    return sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True,
    )
