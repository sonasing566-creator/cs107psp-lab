"""CSV storage functions for VIDYA Analytics."""

import csv
from pathlib import Path


def save_students_csv(students, filename="data/students.csv"):
    """Save student records to a CSV file."""
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    if not students:
        raise ValueError("Student list cannot be empty.")

    fieldnames = list(students[0].keys())

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    return str(path)


def load_students_csv(filename="data/students.csv"):
    """Load student records from a CSV file."""
    path = Path(filename)

    with path.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))
