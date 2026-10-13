"""
Q51: Structured Files — CSV and JSON

Part A:
Write student records to CSV using DictWriter
and read them using DictReader.

Part B:
Save a nested dictionary using json.dump(indent=4)
and reload it using json.load().

Part C:
Compare CSV and JSON.
"""

import csv
import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

CSV_FILE = DATA_DIR / "marks.csv"
JSON_FILE = DATA_DIR / "students.json"

# -----------------------------
# Part A: CSV writing and reading
# -----------------------------

students = [
    {
        "roll": "2626299",
        "name": "Sona",
        "course": "MCA",
        "Python": 85,
        "DBMS": 95,
        "Statistics": 92
    },
    {
        "roll": "2626300",
        "name": "Aman",
        "course": "MCA",
        "Python": 78,
        "DBMS": 82,
        "Statistics": 80
    }
]

fieldnames = [
    "roll", "name", "course",
    "Python", "DBMS", "Statistics"
]

with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("CSV file written successfully.")

with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    csv_records = list(reader)

print("CSV records:")
for record in csv_records:
    print(record)

# Demonstrate csv.writer
with open(DATA_DIR / "marks_simple.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll", "Name", "Course"])
    writer.writerow(["2626299", "Sona", "MCA"])
    writer.writerow(["2626300", "Aman", "MCA"])

print("\nSimple CSV written using csv.writer.")

# -----------------------------
# Part B: JSON writing and reading
# -----------------------------

students_db = {
    "S001": {
        "name": "Sona",
        "course": "MCA",
        "semester": 1,
        "marks": {
            "Python": 85,
            "DBMS": 95,
            "Statistics": 92
        }
    },
    "S002": {
        "name": "Aman",
        "course": "MCA",
        "semester": 1,
        "marks": {
            "Python": 78,
            "DBMS": 82,
            "Statistics": 80
        }
    }
}

with open(JSON_FILE, "w", encoding="utf-8") as file:
    json.dump(students_db, file, indent=4)

print("\nJSON file written successfully.")

with open(JSON_FILE, "r", encoding="utf-8") as file:
    loaded_students = json.load(file)

print("JSON reload successful:", loaded_students == students_db)

# -----------------------------
# Part C: CSV vs JSON
# -----------------------------

print("\nCSV vs JSON:")
print("CSV is best for tabular rows and columns.")
print("JSON is best for nested and hierarchical data.")

print("\nAll Q51 demonstrations completed.")
