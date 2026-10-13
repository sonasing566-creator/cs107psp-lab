"""JSON storage functions for VIDYA Analytics."""

import json
from pathlib import Path


def save_students_json(students, filename="data/students.json"):
    """Save student records to a JSON file."""
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

    return str(path)


def load_students_json(filename="data/students.json"):
    """Load student records from a JSON file."""
    path = Path(filename)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
