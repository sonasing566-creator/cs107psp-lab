"""Student management and validation functions for VIDYA Analytics."""


class InvalidMarkError(ValueError):
    """Raised when student marks are invalid."""


def validate_marks(marks):
    """Validate that marks are between 0 and 100."""
    try:
        marks = float(marks)
    except (ValueError, TypeError):
        raise InvalidMarkError("Marks must be a number.")

    if not 0 <= marks <= 100:
        raise InvalidMarkError("Marks must be between 0 and 100.")

    return marks


def add_student(students, student_id, name, marks):
    """Add a student with a unique ID."""
    student_id = str(student_id).strip()
    name = name.strip()

    if not student_id:
        raise ValueError("Student ID cannot be empty.")
    if not name:
        raise ValueError("Student name cannot be empty.")
    if any(s["id"] == student_id for s in students):
        raise ValueError("Student ID already exists.")

    students.append({
        "id": student_id,
        "name": name,
        "marks": validate_marks(marks),
    })


def search_student(students, student_id):
    """Find a student by ID."""
    for student in students:
        if student["id"] == str(student_id).strip():
            return student
    return None


def update_student(students, student_id, name=None, marks=None):
    """Update a student's name or marks."""
    student = search_student(students, student_id)

    if student is None:
        return False

    if name is not None:
        name = name.strip()
        if not name:
            raise ValueError("Student name cannot be empty.")
        student["name"] = name

    if marks is not None:
        student["marks"] = validate_marks(marks)

    return True


def delete_student(students, student_id):
    """Delete a student by ID."""
    student = search_student(students, student_id)

    if student is None:
        return False

    students.remove(student)
    return True
