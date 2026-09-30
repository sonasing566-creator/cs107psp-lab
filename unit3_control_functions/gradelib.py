"""
gradelib.py
Reusable grading and student-analysis functions for VIDYA ANALYTICS.
Q36: Unit-3 grading engine
"""


# =========================
# Q32 — Functions
# =========================

def calculate_total(marks):
    """Return the total of all marks."""
    return sum(marks)


def calculate_average(marks):
    """Return the average of all marks."""
    return sum(marks) / len(marks)


def calculate_grade(percentage):
    """Return a grade based on percentage."""
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


def create_marksheet(name, roll_number, marks):
    """Return a dictionary containing a student's marksheet."""
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    return {
        "name": name,
        "roll_number": roll_number,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }


# =========================
# Q33 — Arguments
# =========================

def report(name, roll, *marks, college="ABC Institute", **extra):
    """Return a student report using positional, variable and keyword arguments."""
    return {
        "name": name,
        "roll": roll,
        "marks": marks,
        "college": college,
        "extra": extra
    }


# =========================
# Q34 — Multiple Returns
# =========================

def analyse(marks):
    """Return total, average, highest and lowest marks."""
    total = sum(marks)
    avg = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return total, avg, highest, lowest


def assign_grade(mark):
    """Return a grade letter using the Q34 grading rules."""
    return (
        "A" if mark >= 85
        else "B" if mark >= 70
        else "C" if mark >= 40
        else "D"
    )


def add_bonus(mark):
    """Add 5 bonus marks without exceeding 100."""
    return min(mark + 5, 100)


def eligible_for_bonus(mark):
    """Return True when a mark is eligible for bonus marks."""
    return mark >= 40


# =========================
# Q35 — Recursion
# =========================

def factorial(n):
    """Return n factorial using recursion."""
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def fibonacci_recursive(n):
    """Return the nth Fibonacci number using recursion."""
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def sum_digits(n):
    """Return the sum of digits of n using recursion."""
    if n == 0:
        return 0

    return (n % 10) + sum_digits(n // 10)


def reverse_string(text):
    """Return a string reversed using recursion."""
    if len(text) <= 1:
        return text

    return text[-1] + reverse_string(text[:-1])


def gcd_recursive(a, b):
    """Return the greatest common divisor using recursion."""
    if b == 0:
        return abs(a)

    return gcd_recursive(b, a % b)


def fibonacci_iterative(n):
    """Return the nth Fibonacci number using iteration."""
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a
