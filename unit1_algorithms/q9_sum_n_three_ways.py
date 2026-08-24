n = 100000

# 1. Sequence: formula
sum_sequence = n * (n + 1) // 2

# 2. Selection: validation + formula
if n > 0:
    sum_selection = n * (n + 1) // 2
else:
    sum_selection = 0

# 3. Iteration: loop
sum_iteration = 0
for i in range(1, n + 1):
    sum_iteration += i

print("N:", n)
print("Sequence sum:", sum_sequence)
print("Selection sum:", sum_selection)
print("Iteration sum:", sum_iteration)
