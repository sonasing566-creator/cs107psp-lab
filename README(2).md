# VIDYA Analytics — Student Result Management System

## Project Overview
VIDYA Analytics is a menu-driven Student Result Management System developed
using Python for the CS107PSP — Problem Solving Using Python course.

## Features
- Add, search, update, and delete student records.
- Validate marks between 0 and 100.
- Prevent duplicate student IDs.
- Calculate grades and pass/fail status.
- Analyse and rank students.
- Save and load records using CSV and JSON.
- Generate timestamped text reports.
- Support command-line arguments using argparse.
- Handle invalid input using exceptions.

## Project Structure
- `vidya/core/grading.py` — Grade and pass/fail calculations.
- `vidya/core/analysis.py` — Marks analysis and ranking.
- `vidya/core/student_manager.py` — Student record management.
- `vidya/core/result_report.py` — Timestamped result reports.
- `vidya/storage/csv_store.py` — CSV storage.
- `vidya/storage/json_store.py` — JSON storage.
- `vidya/cli.py` — Main menu-driven application.
- `data/` — Data files.
- `reports/` — Generated result reports.

## Requirements
- Python 3.11 or later.
- Google Colab or a local Python environment.

## How to Run
From the project directory, run:

`python -m vidya.cli`

Load records from CSV:

`python -m vidya.cli --data-format csv --data-file data/q58_test_students.csv`

Load records from JSON:

`python -m vidya.cli --data-format json --data-file data/q58_test_students.json`

## Menu Options
1. Add student
2. Display all students
3. Search student
4. Update student
5. Delete student
6. Analyse marks
7. Rank students
8. Save students to CSV
9. Load students from CSV
10. Save students to JSON
11. Load students from JSON
12. Generate timestamped report
13. Exit

## Result Reports
The application creates timestamped text reports containing student IDs,
names, marks, grades, rankings, and pass/fail status.

## Validation
Marks must be numeric and between 0 and 100. Duplicate student IDs are
rejected. Invalid marks raise the custom `InvalidMarkError` exception.

## Testing
Tests have been performed for student management, marks validation,
duplicate IDs, CSV and JSON storage, report generation, and command-line
argument parsing.

## Course Information
Course: CS107PSP — Problem Solving Using Python

Project: VIDYA Analytics — Student Result Management System
