"""
Q52: Exception Handling

Demonstrates:
1. try, except, else, finally
2. Common built-in exceptions
3. Raising ValueError for invalid marks
4. Custom InvalidMarkError
5. assert for a sanity check
"""

from pathlib import Path


# Custom exception
class InvalidMarkError(Exception):
    """Raised when a mark is not between 0 and 100."""


# Validate marks using ValueError
def validate_mark(mark):
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")
    return mark


# Validate marks using a custom exception
def check_mark(mark):
    if not 0 <= mark <= 100:
        raise InvalidMarkError("Mark must be between 0 and 100.")
    return mark


# Demonstrate try, except, else, finally with file opening
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: File was not found.")

    except ValueError:
        print("Error: Invalid value while reading the file.")

    except Exception as e:
        print("Unexpected error type:", type(e).__name__)

    else:
        print("File opened and read successfully.")
        print("Content:", content)

    finally:
        print("File operation finished.")


# Demonstrate separate exception handling
def demonstrate_exceptions():
    print("\n1. FileNotFoundError")
    try:
        open("data/file_that_does_not_exist.txt", "r")
    except FileNotFoundError:
        print("FileNotFoundError caught.")

    print("\n2. ValueError")
    try:
        int("hello")
    except ValueError:
        print("ValueError caught.")

    print("\n3. KeyError")
    try:
        student = {"name": "Sona"}
        print(student["marks"])
    except KeyError:
        print("KeyError caught.")

    print("\n4. ZeroDivisionError")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError caught.")

    print("\n5. IndexError")
    try:
        numbers = [10, 20, 30]
        print(numbers[5])
    except IndexError:
        print("IndexError caught.")

    print("\n6. Last-resort Exception handler")
    try:
        result = 10 / 0
    except Exception as e:
        print("Last-resort handler caught:", type(e).__name__)


# Demonstrate mark validation
def demonstrate_mark_validation():
    print("\n7. ValueError for invalid marks")
    try:
        validate_mark(105)
    except ValueError as e:
        print("ValueError caught:", e)

    print("\n8. Custom InvalidMarkError")
    try:
        check_mark(-5)
    except InvalidMarkError as e:
        print("Custom exception caught:", e)

    print("\n9. Valid mark")
    print("Validated mark:", check_mark(85))


# Main program
if __name__ == "__main__":
    print("Q52: Exception Handling")

    # Create a sample file for successful reading
    sample_file = Path("data/q52_sample.txt")
    sample_file.parent.mkdir(parents=True, exist_ok=True)
    sample_file.write_text(
        "Student: Sona\nMarks: 85\n",
        encoding="utf-8"
    )

    print("\n10. Successful file opening")
    read_file(str(sample_file))

    print("\n11. Missing file")
    read_file("data/missing_q52_file.txt")

    demonstrate_exceptions()
    demonstrate_mark_validation()

    # Quick sanity check
    assert validate_mark(85) == 85
    assert check_mark(100) == 100
    print("\n12. Assertion passed: valid marks are accepted.")

    print("\nAll Q52 demonstrations completed.")
