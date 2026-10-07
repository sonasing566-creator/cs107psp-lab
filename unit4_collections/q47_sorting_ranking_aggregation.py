"""
Q47: Sorting, Ranking and Aggregation
"""

from collections import Counter
from statistics import mean

print("===== Q47: SORTING, RANKING AND AGGREGATION =====")

db = {
    "S001": {
        "name": "Sona",
        "course": "MCA",
        "semester": 1,
        "marks": {"Python": 90, "DBMS": 78, "Statistics": 92}
    },
    "S002": {
        "name": "Aman",
        "course": "MCA",
        "semester": 1,
        "marks": {"Python": 72, "DBMS": 81, "Statistics": 75}
    },
    "S003": {
        "name": "Riya",
        "course": "MCA",
        "semester": 1,
        "marks": {"Python": 90, "DBMS": 95, "Statistics": 88}
    },
    "S004": {
        "name": "Rahul",
        "course": "MCA",
        "semester": 1,
        "marks": {"Python": 65, "DBMS": 70, "Statistics": 68}
    }
}

print("\n===== PERCENTAGE =====")

for roll, details in db.items():
    marks = details["marks"]
    total = sum(marks.values())
    percentage = total / len(marks)
    details["total"] = total
    details["percentage"] = percentage

    print(
        roll,
        details["name"],
        "Total:", total,
        "Percentage:", round(percentage, 2)
    )


print("\n===== RANK LIST =====")

rank_list = sorted(
    db.items(),
    key=lambda x: x[1]["percentage"],
    reverse=True
)

for rank, (roll, details) in enumerate(rank_list, start=1):
    print(
        "Rank:", rank,
        "| Roll:", roll,
        "| Name:", details["name"],
        "| Percentage:", round(details["percentage"], 2)
    )


print("\n===== SUBJECT-WISE TOPPER =====")

subjects = ["Python", "DBMS", "Statistics"]

for subject in subjects:
    topper = max(
        db.items(),
        key=lambda x: x[1]["marks"][subject]
    )

    roll, details = topper

    print(
        subject,
        "->",
        details["name"],
        "| Marks:", details["marks"][subject]
    )


print("\n===== GRADE DISTRIBUTION =====")

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "F"


grades = []

for details in db.values():
    grade = calculate_grade(details["percentage"])
    details["grade"] = grade
    grades.append(grade)

grade_distribution = Counter(grades)

print(grade_distribution)


print("\n===== SUBJECT AVERAGES =====")

for subject in subjects:
    subject_marks = [
        details["marks"][subject]
        for details in db.values()
    ]

    average = mean(subject_marks)

    print(subject, "Average:", round(average, 2))


print("\n===== Q47 COMPLETE =====")
