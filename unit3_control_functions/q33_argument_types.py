"""
Q33: Argument Types

Demonstrates:
1. Positional arguments
2. Keyword arguments
3. Default arguments
4. *args
5. **kwargs
6. Positional argument after keyword argument error
7. Mutable default argument trap and its fix
"""


def report(name, roll, *marks, college="ABC Institute", **extra):
    """Display student report using different argument types."""
    print("\n===== REPORT =====")
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print(f"College: {college}")
    print(f"Marks: {marks}")
    print(f"Extra Details: {extra}")


# 1. Positional arguments
print("\n--- 1. Positional Arguments ---")
report("Sona", "2626299", 85, 78, 92)


# 2. Keyword arguments
print("\n--- 2. Keyword Arguments ---")
report(
    name="Sona",
    roll="2626299",
    college="ABC Institute",
    city="Haridwar"
)


# 3. Default argument
print("\n--- 3. Default Argument ---")
report("Sona", "2626299", 90, 88)


# 4. *args
print("\n--- 4. *args ---")
report("Sona", "2626299", 85, 90, 78, 88, 92)


# 5. **kwargs
print("\n--- 5. **kwargs ---")
report(
    "Sona",
    "2626299",
    85,
    90,
    college="ABC Institute",
    city="Haridwar",
    course="MCA"
)


# Positional argument after keyword argument
print("\n--- Positional After Keyword Error ---")

try:
    eval('report(name="Sona", "2626299")')
except SyntaxError as error:
    print("SyntaxError:", error)


# Mutable default argument trap
print("\n--- Mutable Default Argument Trap ---")


def f(x, lst=[]):
    lst.append(x)
    return lst


print("f(1):", f(1))
print("f(2):", f(2))
print("f(3):", f(3))


# Fixed version
print("\n--- Fixed Mutable Default Argument ---")


def fixed_f(x, lst=None):
    if lst is None:
        lst = []

    lst.append(x)
    return lst


print("fixed_f(1):", fixed_f(1))
print("fixed_f(2):", fixed_f(2))
print("fixed_f(3):", fixed_f(3))
