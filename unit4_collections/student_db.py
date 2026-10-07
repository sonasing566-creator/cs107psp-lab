"""
Q48: Unit-4 Consolidation
Menu-driven in-memory Student Database

Known limitation:
All data is lost when the program exits.
"""

import sys

# Import gradelib from Q36
sys.path.append("unit3_control_functions")

from gradelib import calculate_total, calculate_average, calculate_grade


# Dictionary:
# roll number -> student details
students = {}


def add_student():
    print("\n--- ADD STUDENT ---")

    roll = input("Enter roll number: ")

    if roll in students:
        print("Student already exists.")
        return

    name = input("Enter name: ")
    course = input("Enter course: ")

    marks = []

    subjects = ("Python", "DBMS", "Statistics")

    for subject in subjects:
        mark = float(input(f"Enter {subject} marks: "))
        marks.append(mark)

    students[roll] = {
        "name": name,
        "course": course,
        "marks": marks
    }

    print("Student added successfully.")


def display_all():
    print("\n--- ALL STUDENTS ---")

    if not students:
        print("No students found.")
        return

    for roll, details in students.items():
        total = calculate_total(details["marks"])
        average = calculate_average(details["marks"])
        grade = calculate_grade(average)

        print(
            f"Roll: {roll} | "
            f"Name: {details['name']} | "
            f"Course: {details['course']} | "
            f"Marks: {details['marks']} | "
            f"Average: {average:.2f} | "
            f"Grade: {grade}"
        )


def search_student():
    print("\n--- SEARCH BY ROLL ---")

    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    details = students[roll]

    print("Roll:", roll)
    print("Name:", details["name"])
    print("Course:", details["course"])
    print("Marks:", details["marks"])


def update_marks():
    print("\n--- UPDATE MARKS ---")

    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    subjects = ("Python", "DBMS", "Statistics")
    marks = []

    for subject in subjects:
        mark = float(input(f"Enter new {subject} marks: "))
        marks.append(mark)

    students[roll]["marks"] = marks

    print("Marks updated successfully.")


def delete_student():
    print("\n--- DELETE STUDENT ---")

    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    del students[roll]

    print("Student deleted successfully.")


def rank_list():
    print("\n--- RANK LIST ---")

    if not students:
        print("No students found.")
        return

    ranked = sorted(
        students.items(),
        key=lambda x: calculate_average(x[1]["marks"]),
        reverse=True
    )

    for rank, (roll, details) in enumerate(ranked, start=1):
        average = calculate_average(details["marks"])

        print(
            f"Rank: {rank} | "
            f"Roll: {roll} | "
            f"Name: {details['name']} | "
            f"Percentage: {average:.2f}"
        )


def subject_analysis():
    print("\n--- SUBJECT ANALYSIS ---")

    if not students:
        print("No students found.")
        return

    subjects = ("Python", "DBMS", "Statistics")

    for index, subject in enumerate(subjects):
        subject_marks = [
            details["marks"][index]
            for details in students.values()
        ]

        average = calculate_average(subject_marks)
        topper_index = subject_marks.index(max(subject_marks))

        rolls = list(students.keys())
        topper_roll = rolls[topper_index]
        topper_name = students[topper_roll]["name"]

        print(
            f"{subject} | "
            f"Average: {average:.2f} | "
            f"Topper: {topper_name} | "
            f"Marks: {max(subject_marks):.2f}"
        )


def show_menu():
    print("\n==============================")
    print("   STUDENT DATABASE")
    print("==============================")
    print("1. Add student")
    print("2. Display all")
    print("3. Search by roll")
    print("4. Update marks")
    print("5. Delete student")
    print("6. Rank list")
    print("7. Subject analysis")
    print("8. Exit")
    print("==============================")


def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_all()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_marks()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            rank_list()

        elif choice == "7":
            subject_analysis()

        elif choice == "8":
            print("Exiting Student Database.")
            print("Note: All data will be lost after exit.")
            break

        else:
            print("Invalid choice. Please enter 1-8.")


if __name__ == "__main__":
    main()
