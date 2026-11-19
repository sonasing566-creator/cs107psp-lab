"""Generate timestamped student result reports."""

from datetime import datetime
from pathlib import Path

from vidya.core.grading import assign_grade, is_pass
from vidya.core.analysis import rank_students


def generate_result_report(students, output_dir="reports"):
    """Create a timestamped text report of student results."""
    report_dir = Path(output_dir)
    report_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = report_dir / f"student_results_{timestamp}.txt"

    lines = [
        "VIDYA STUDENT RESULT REPORT",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 40,
        "",
    ]

    if not students:
        lines.append("No student records available.")
    else:
        for rank, student in enumerate(rank_students(students), start=1):
            marks = float(student["marks"])
            grade = assign_grade(marks)
            status = "PASS" if is_pass(marks) else "FAIL"

            lines.append(
                f"Rank: {rank} | ID: {student['id']} | "
                f"Name: {student['name']} | Marks: {marks:.2f} | "
                f"Grade: {grade} | Status: {status}"
            )

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(report_path)
