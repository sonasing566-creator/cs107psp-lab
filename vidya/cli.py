"""Menu-driven Student Result Management System for VIDYA Analytics."""

import argparse

from vidya.core.grading import calculate_percentage, assign_grade, is_pass
from vidya.core.analysis import analyse_marks, rank_students
from vidya.core.student_manager import (
    add_student,
    search_student,
    update_student,
    delete_student,
    InvalidMarkError,
)
from vidya.storage.csv_store import save_students_csv, load_students_csv
from vidya.storage.json_store import save_students_json, load_students_json
from vidya.core.result_report import generate_result_report


def parse_arguments(args=None):
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="VIDYA Student Result Management System"
    )
    parser.add_argument(
        "--data-format",
        choices=["csv", "json"],
        default="json",
        help="Data format to load at startup",
    )
    parser.add_argument(
        "--data-file",
        default=None,
        help="Optional path to the data file",
    )
    return parser.parse_args(args)


def main(argv=None):
    """Run the interactive student management menu."""
    args = parse_arguments(argv)
    students = []

    if args.data_file:
        try:
            if args.data_format == "csv":
                students = load_students_csv(args.data_file)
            else:
                students = load_students_json(args.data_file)

            for student in students:
                student["id"] = str(student["id"])
                student["marks"] = float(student["marks"])

            print(f"Loaded {len(students)} students.")
        except (FileNotFoundError, ValueError, KeyError) as error:
            print("Could not load data:", error)

    while True:
        print("\n===== VIDYA STUDENT RESULT MANAGEMENT =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Analyse marks")
        print("7. Rank students")
        print("8. Save students to CSV")
        print("9. Load students from CSV")
        print("10. Save students to JSON")
        print("11. Load students from JSON")
        print("12. Generate timestamped report")
        print("13. Exit")

        choice = input("Enter your choice (1-13): ").strip()

        if choice == "1":
            try:
                student_id = input("Enter student ID: ").strip()
                name = input("Enter student name: ").strip()
                marks = input("Enter marks out of 100: ")
                add_student(students, student_id, name, marks)
                print("Student added successfully.")
            except (ValueError, InvalidMarkError) as error:
                print("Error:", error)

        elif choice == "2":
            if not students:
                print("No students available.")
            else:
                for student in students:
                    percentage = calculate_percentage(student["marks"], 100)
                    grade = assign_grade(percentage)
                    status = "PASS" if is_pass(percentage) else "FAIL"
                    print(
                        f"ID: {student['id']} | Name: {student['name']} | "
                        f"Marks: {student['marks']} | Grade: {grade} | "
                        f"Status: {status}"
                    )

        elif choice == "3":
            student_id = input("Enter student ID to search: ").strip()
            student = search_student(students, student_id)
            print(student if student else "Student not found.")

        elif choice == "4":
            student_id = input("Enter student ID to update: ").strip()
            student = search_student(students, student_id)

            if student is None:
                print("Student not found.")
            else:
                print("Leave a field blank to keep its current value.")
                name = input(f"New name [{student['name']}]: ").strip()
                marks_input = input(f"New marks [{student['marks']}]: ").strip()

                try:
                    update_student(
                        students,
                        student_id,
                        name=name if name else None,
                        marks=marks_input if marks_input else None,
                    )
                    print("Student updated successfully.")
                except (ValueError, InvalidMarkError) as error:
                    print("Error:", error)

        elif choice == "5":
            student_id = input("Enter student ID to delete: ").strip()
            if delete_student(students, student_id):
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        elif choice == "6":
            if not students:
                print("Add students first.")
            else:
                print(analyse_marks([student["marks"] for student in students]))

        elif choice == "7":
            if not students:
                print("Add students first.")
            else:
                for position, student in enumerate(rank_students(students), 1):
                    print(
                        f"{position}. {student['name']} "
                        f"(ID: {student['id']}) - {student['marks']} marks"
                    )

        elif choice == "8":
            try:
                print("Saved to:", save_students_csv(students))
            except ValueError as error:
                print("Error:", error)

        elif choice == "9":
            try:
                students = load_students_csv()
                for student in students:
                    student["id"] = str(student["id"])
                    student["marks"] = float(student["marks"])
                print(f"Loaded {len(students)} students from CSV.")
            except (FileNotFoundError, ValueError, KeyError) as error:
                print("Could not load CSV:", error)

        elif choice == "10":
            print("Saved to:", save_students_json(students))

        elif choice == "11":
            try:
                students = load_students_json()
                for student in students:
                    student["id"] = str(student["id"])
                    student["marks"] = float(student["marks"])
                print(f"Loaded {len(students)} students from JSON.")
            except (FileNotFoundError, ValueError, KeyError) as error:
                print("Could not load JSON:", error)

        elif choice == "12":
            try:
                report_path = generate_result_report(students)
                print("Report created:", report_path)
            except (OSError, ValueError) as error:
                print("Could not create report:", error)

        elif choice == "13":
            print("Thank you for using VIDYA Analytics.")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 12.")


if __name__ == "__main__":
    main()
