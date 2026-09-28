
# Q20: Bitwise, Membership and Identity Operators

# (a) Bitwise operators on two roll numbers
roll1 = 26
roll2 = 29

print("Part (a): Bitwise Operators")
print("Roll Number 1:", roll1, "Binary:", bin(roll1))
print("Roll Number 2:", roll2, "Binary:", bin(roll2))
print()

print("AND (&):", roll1 & roll2, bin(roll1 & roll2))
print("OR  (|):", roll1 | roll2, bin(roll1 | roll2))
print("XOR (^):", roll1 ^ roll2, bin(roll1 ^ roll2))
print("NOT (~):", ~roll1, bin(~roll1))
print("Left Shift (<<):", roll1 << 1, bin(roll1 << 1))
print("Right Shift (>>):", roll1 >> 1, bin(roll1 >> 1))


# (b) Membership operators
print("\nPart (b): Membership Operators")

subject = "Python"
subjects = ["Python", "DBMS", "Statistics", "Cloud Computing"]

print("'Python' in subject:", "Python" in subject)
print("'Java' not in subject:", "Java" not in subject)

print("'DBMS' in subjects:", "DBMS" in subjects)
print("'Java' not in subjects:", "Java" not in subjects)


# (c) Identity vs Equality
print("\nPart (c): Identity vs Equality")

list1 = ["Python", "DBMS", "Statistics"]
list2 = ["Python", "DBMS", "Statistics"]
list3 = list1

print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)
print("list1 is not list2:", list1 is not list2)

print("\nlist1 == list3:", list1 == list3)
print("list1 is list3:", list1 is list3)

print("\nExplanation:")
print("== checks whether two objects have equal values.")
print("is checks whether two variables refer to the same object.")
