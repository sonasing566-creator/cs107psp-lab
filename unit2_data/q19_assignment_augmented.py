
# Q19: Assignment and Augmented Assignment Operators

total = 0
print("Initial total:", total)

# +=
total += 10
print("After += 10:", total)

# -=
total -= 3
print("After -= 3:", total)

# *=
total *= 2
print("After *= 2:", total)

# /=
total /= 7
print("After /= 7:", total)

# //=
total //= 2
print("After //= 2:", total)

# %=
total %= 3
print("After %= 3:", total)

# **=
total **= 2
print("After **= 2:", total)


# Difference with lists
print("\nLists and += vs =")

list1 = [1, 2]
list2 = list1

list1 = list1 + [3]
print("After list1 = list1 + [3]:")
print("list1:", list1)
print("list2:", list2)

list3 = [1, 2]
list4 = list3

list3 += [3]
print("\nAfter list3 += [3]:")
print("list3:", list3)
print("list4:", list4)

print("\nExplanation:")
print("list = list + x creates a new list.")
print("list += x modifies the existing list in-place.")
