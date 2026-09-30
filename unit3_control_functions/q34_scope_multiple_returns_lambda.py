
"""
Q34: Scope, Multiple Returns and Lambda

Demonstrates:
1. Local and global scope
2. global and nonlocal keywords
3. Multiple return values and tuple unpacking
4. lambda, map() and filter()
"""

# Part (a): Local vs Global Scope

global_message = "This is a global variable"


def scope_demo():
    local_message = "This is a local variable"

    print("Inside function - Local:", local_message)
    print("Inside function - Global:", global_message)


scope_demo()

print("Outside function - Global:", global_message)


# Demonstrate global keyword
counter = 0


def increase_counter():
    global counter
    counter += 1
    return counter


print("\nGlobal keyword:")
print("Counter:", increase_counter())
print("Counter:", increase_counter())


# Demonstrate nonlocal keyword
def outer_function():
    message = "Outer message"

    def inner_function():
        nonlocal message
        message = "Changed by inner function"

    inner_function()
    return message


print("\nNonlocal keyword:")
print(outer_function())


# Part (b): Multiple Returns

def analyse(marks):
    total = sum(marks)
    avg = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return total, avg, highest, lowest


marks = [85, 78, 92, 88, 90]

total, avg, highest, lowest = analyse(marks)

print("\nMultiple Return Values:")
print("Marks:", marks)
print("Total:", total)
print("Average:", avg)
print("Highest:", highest)
print("Lowest:", lowest)


# Part (c): lambda, map() and filter()

marks_with_bonus = [35, 45, 60, 72, 88]

# Lambda for grade calculation
assign_grade = lambda mark: (
    "A" if mark >= 85
    else "B" if mark >= 70
    else "C" if mark >= 40
    else "D"
)

grades = list(map(assign_grade, marks_with_bonus))

print("\nLambda + map():")
print("Marks:", marks_with_bonus)
print("Grades:", grades)


# Lambda for bonus marks
add_bonus = lambda mark: min(mark + 5, 100)

bonus_marks = list(map(add_bonus, marks_with_bonus))

print("\nmap() with bonus:")
print("Original Marks:", marks_with_bonus)
print("Bonus Marks:", bonus_marks)


# filter() for students eligible for bonus
eligible_marks = list(filter(lambda mark: mark >= 40, marks_with_bonus))

print("\nfilter():")
print("Eligible Marks (>= 40):", eligible_marks)
