"""Command-line interface for VIDYA Analytics."""

from vidya.core.grading import calculate_percentage, assign_grade, is_pass
from vidya.core.analysis import analyse_marks, rank_students
from vidya.storage.csv_store import save_students_csv, load_students_csv
from vidya.storage.json_store import save_students_json, load_students_json


def main():
    students = []

    while True:
        print("\n===== VIDYA ANALYTICS =====")
        print("1. Add student")
        print("2. Display students")
        print("3. Analyse marks")
        print("4. Rank students")
        print("5. Save students to CSV")
        print("6. Load students from CSV")
        print("7. Save students to JSON")
        print("8. Load students from JSON")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()

            try:
                marks = float(input("Enter marks out of 100: "))
                if not 0 <= marks <= 100:
                    raise ValueError("Marks must be between 0 and 100.")

                students.append({"name": name, "marks": marks})
                print("Student added successfully.")
            except ValueError as error:
                print("Invalid input:", error)

        elif choice == "2":
            if not students:
                print("No students available.")
            else:
                for student in students:
                    percentage = calculate_percentage(student["marks"], 100)
                    grade = assign_grade(percentage)
                    status = "PASS" if is_pass(percentage) else "FAIL"
                    print(
                        f"Name: {student['name']}, "
                        f"Marks: {student['marks']}, "
                        f"Grade: {grade}, Status: {status}"
                    )

        elif choice == "3":
            if not students:
                print("Add students first.")
            else:
                marks_list = [student["marks"] for student in students]
                print(analyse_marks(marks_list))

        elif choice == "4":
            if not students:
                print("Add students first.")
            else:
                for position, student in enumerate(
                    rank_students(students), start=1
                ):
                    print(
                        f"{position}. {student['name']} "
                        f"- {student['marks']} marks"
                    )

        elif choice == "5":
            if not students:
                print("No students to save.")
            else:
                print("Saved to:", save_students_csv(students))

        elif choice == "6":
            try:
                students = load_students_csv()
                for student in students:
                    student["marks"] = float(student["marks"])
                print(f"Loaded {len(students)} students from CSV.")
            except (FileNotFoundError, KeyError, ValueError) as error:
                print("Could not load CSV:", error)

        elif choice == "7":
            print("Saved to:", save_students_json(students))

        elif choice == "8":
            try:
                students = load_students_json()
                print(f"Loaded {len(students)} students from JSON.")
            except (FileNotFoundError, ValueError) as error:
                print("Could not load JSON:", error)

        elif choice == "9":
            print("Thank you for using VIDYA Analytics.")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
