"""
Q39: List Operations, Aliasing and Cloning

Demonstrates:
1. + operator
2. * operator
3. in operator
4. List iteration
5. Aliasing using b = a
6. Shallow cloning using a.copy()
7. Slicing clone using a[:]
8. Deep cloning using copy.deepcopy()
9. id() comparison
"""

import copy


print("===== LIST OPERATIONS =====")

subjects = ["Python", "DBMS", "Statistics"]

print("Original subjects:", subjects)

# + operator
combined = subjects + ["Cloud Computing"]
print("\nUsing + operator:")
print("Combined list:", combined)

# * operator
repeated = ["Python", "DBMS"] * 2
print("\nUsing * operator:")
print("Repeated list:", repeated)

# in operator
print("\nUsing in operator:")
print("'Python' in subjects:", "Python" in subjects)
print("'AI' in subjects:", "AI" in subjects)

# Iteration
print("\n===== LIST ITERATION =====")
for subject in subjects:
    print("Subject:", subject)


print("\n===== ALIASING: b = a =====")

a = ["Python", ["DBMS", "Statistics"]]
b = a

print("a:", a)
print("b:", b)
print("id(a):", id(a))
print("id(b):", id(b))
print("Same object:", a is b)

b[0] = "AI"

print("\nAfter b[0] = 'AI':")
print("a:", a)
print("b:", b)
print("Both changed because b is an alias of a.")


print("\n===== SHALLOW COPY: b = a.copy() =====")

a = ["Python", ["DBMS", "Statistics"]]
b = a.copy()

print("a:", a)
print("b:", b)
print("id(a):", id(a))
print("id(b):", id(b))
print("Same outer object:", a is b)

b[0] = "AI"

print("\nAfter b[0] = 'AI':")
print("a:", a)
print("b:", b)

b[1][0] = "Data Science"

print("\nAfter b[1][0] = 'Data Science':")
print("a:", a)
print("b:", b)
print("Nested list also changed because copy() is shallow.")


print("\n===== SLICING COPY: b = a[:] =====")

a = ["Python", ["DBMS", "Statistics"]]
b = a[:]

print("a:", a)
print("b:", b)
print("id(a):", id(a))
print("id(b):", id(b))
print("Same outer object:", a is b)

b[0] = "AI"

print("\nAfter b[0] = 'AI':")
print("a:", a)
print("b:", b)

b[1][0] = "Data Science"

print("\nAfter b[1][0] = 'Data Science':")
print("a:", a)
print("b:", b)
print("Nested list also changed because slicing is shallow.")


print("\n===== DEEP COPY: copy.deepcopy(a) =====")

a = ["Python", ["DBMS", "Statistics"]]
b = copy.deepcopy(a)

print("a:", a)
print("b:", b)
print("id(a):", id(a))
print("id(b):", id(b))
print("Same outer object:", a is b)

print("id(a[1]):", id(a[1]))
print("id(b[1]):", id(b[1]))
print("Same nested object:", a[1] is b[1])

b[1][0] = "Data Science"

print("\nAfter b[1][0] = 'Data Science':")
print("a:", a)
print("b:", b)
print("Original nested list is unchanged.")


print("\n===== ID COMPARISON SUMMARY =====")
original = ["Python", ["DBMS", "Statistics"]]

alias = original
shallow_copy = original.copy()
slice_copy = original[:]
deep_copy = copy.deepcopy(original)

print("id(original):", id(original))
print("id(alias):", id(alias))
print("id(shallow_copy):", id(shallow_copy))
print("id(slice_copy):", id(slice_copy))
print("id(deep_copy):", id(deep_copy))

print("\nNested list IDs:")
print("id(original[1]):", id(original[1]))
print("id(alias[1]):", id(alias[1]))
print("id(shallow_copy[1]):", id(shallow_copy[1]))
print("id(slice_copy[1]):", id(slice_copy[1]))
print("id(deep_copy[1]):", id(deep_copy[1]))


print("\n===== VIVA =====")
print("Why is aliasing a common beginner bug?")
print(
    "Because b = a does not create a new list. "
    "Both variables refer to the same object, so changing one also changes the other."
)

print("\n===== Q39 COMPLETE =====")
