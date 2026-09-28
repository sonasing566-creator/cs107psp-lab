
# Q18: Relational and Logical Operators - Eligibility Check

attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter internal marks: "))

attendance_ok = attendance >= 75
marks_ok = marks >= 40

eligible_and = attendance_ok and marks_ok
eligible_or = attendance_ok or marks_ok
not_eligible = not eligible_and

print("\nEligibility Results:")
print("Attendance >= 75:", attendance_ok)
print("Marks >= 40:", marks_ok)
print("Attendance >= 75 AND Marks >= 40:", eligible_and)
print("Attendance >= 75 OR Marks >= 40:", eligible_or)
print("NOT eligible:", not_eligible)


# Truth Table using nested loops
print("\nTruth Table")
print("A       B       A AND B   A OR B    NOT A")

values = [True, False]

for a in values:
    for b in values:
        print(f"{str(a):<7} {str(b):<7} {str(a and b):<9} {str(a or b):<9} {str(not a)}")


# Bonus: Short-circuit evaluation
print("\nShort-Circuit Evaluation")

def check_marks():
    print("check_marks() was evaluated")
    return True

print("False AND check_marks():")
result1 = False and check_marks()
print("Result:", result1)

print("\nTrue OR check_marks():")
result2 = True or check_marks()
print("Result:", result2)
