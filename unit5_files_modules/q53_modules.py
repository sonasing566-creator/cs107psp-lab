"""
Q53: Modules

Demonstrates:
- Creating and importing a custom module
- Four import styles
- __name__ == "__main__"
- dir() and help()
- Standard modules: math, random, os, sys, datetime, statistics
"""

import math
import random
import os
import sys
import statistics
from datetime import datetime
from pathlib import Path

# Make mathutils importable when this script runs from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Import style 1
import mathutils

# Import style 2
import mathutils as mu

# Import style 3
from mathutils import average

# Import style 4
from mathutils import *

# Demonstrate all import styles
def demonstrate_imports():
    print("\n1. IMPORT STYLES")
    print("import mathutils:", mathutils.average([80, 90, 70]))
    print("import mathutils as mu:", mu.grade(95))
    print("from mathutils import average:", average([50, 60, 70]))
    print("from mathutils import *:", grade(75))

    print("\n2. DIR AND HELP")
    print("Available names:", dir(mathutils))
    print("\nHelp for average():")
    help(mathutils.average)


def demonstrate_standard_modules():
    print("\n3. MATH MODULE")
    print("Square root of 144:", math.sqrt(144))
    print("Ceiling of 85.3:", math.ceil(85.3))
    print("Pi:", math.pi)

    print("\n4. RANDOM MODULE")
    random.seed(42)
    marks = [random.randint(0, 100) for _ in range(30)]
    print("30 random marks:", marks)
    print("Number of marks:", len(marks))

    print("\n5. OS MODULE")
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    print("Files in data/:", os.listdir(data_dir))

    print("\n6. SYS MODULE")
    print("Python version:", sys.version)
    print("Python executable:", sys.executable)
    print("Platform:", sys.platform)

    print("\n7. DATETIME MODULE")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Report timestamp:", timestamp)

    print("\n8. STATISTICS MODULE")
    print("Mean:", statistics.mean(marks))
    print("Median:", statistics.median(marks))
    print("Mode:", statistics.mode(marks))
    print("Standard deviation:", round(statistics.stdev(marks), 2))

    # Save a timestamped report
    report_file = data_dir / "q53_report.txt"
    with open(report_file, "w", encoding="utf-8") as file:
        file.write("Q53 Python Modules Report\n")
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Marks: {marks}\n")
        file.write(f"Mean: {statistics.mean(marks):.2f}\n")
        file.write(f"Median: {statistics.median(marks):.2f}\n")
        file.write(f"Mode: {statistics.mode(marks)}\n")
        file.write(
            f"Standard deviation: {statistics.stdev(marks):.2f}\n"
        )

    print("Timestamped report saved to:", report_file)


if __name__ == "__main__":
    print("Q53: Modules practical running directly.")
    demonstrate_imports()
    demonstrate_standard_modules()
    print("\nAll Q53 demonstrations completed.")
