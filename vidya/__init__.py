"""VIDYA Analytics: Student Performance Analytics System."""

__version__ = "1.0.0"

from vidya.core.grading import assign_grade, calculate_percentage, is_pass
from vidya.core.analysis import analyse_marks, rank_students
from vidya.storage.csv_store import save_students_csv, load_students_csv
from vidya.storage.json_store import save_students_json, load_students_json

__all__ = [
    "__version__",
    "assign_grade",
    "calculate_percentage",
    "is_pass",
    "analyse_marks",
    "rank_students",
    "save_students_csv",
    "load_students_csv",
    "save_students_json",
    "load_students_json",
]
