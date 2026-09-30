
"""
Q28: while loop - Menu-Driven Student Marks Entry

This program uses while True to display a menu.
The user can enter student marks, show the mark sheet,
or exit the program.
"""

student_name = ""
roll_number = ""
marks = []

while True:
    print("\n===== STUDENT MENU =====")
    print("1. Enter student marks")
    print("2. Show mark sheet")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")

        marks = []
        for i in range(1, 6):
            mark = float(input(f"Enter marks for Subject {i}: "))
            marks.append(mark)

        print("Student marks entered successfully.")

    elif choice == "2":
        if len(marks) == 5:
            total = sum(marks)
            percentage = (total / 500) * 100

            print("\n===== MARK SHEET =====")
            print(f"Student Name: {student_name}")
            print(f"Roll Number: {roll_number}")

            for i, mark in enumerate(marks, start=1):
                print(f"Subject {i}: {mark:.2f}")

            print(f"Total Marks: {total:.2f}")
            print(f"Percentage: {percentage:.2f}%")
        else:
            print("Please enter student marks first.")

    elif choice == "3":
        print("Program exited.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
