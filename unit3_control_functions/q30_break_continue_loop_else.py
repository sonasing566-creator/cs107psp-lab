"""
Q30: break, continue and loop-else - Input Validation

This program validates marks using continue and break.
It also demonstrates for-else and pass.
"""

print("===== MARKS INPUT VALIDATION =====")

total_marks = 0
valid_count = 0

for i in range(1, 6):
    mark = float(input(f"Enter marks {i} (-1 to stop): "))

    # Sentinel value: stop input early
    if mark == -1:
        print("Input stopped by user.")
        break

    # Reject invalid marks
    if mark < 0 or mark > 100:
        print("Invalid marks. Please enter 0 to 100.")
        continue

    total_marks += mark
    valid_count += 1
    print(f"Valid mark: {mark}")

else:
    print("All marks valid")

# Demonstration of pass
if valid_count == 0:
    pass

print("\n===== RESULT =====")
print(f"Valid Marks Entered: {valid_count}")
print(f"Total Marks: {total_marks:.2f}")
