def gcd_iterative(a, b):
    count = 0

    while b != 0:
        a, b = b, a % b
        count += 1

    return a, count


def gcd_recursive(a, b):
    if b == 0:
        return a

    return gcd_recursive(b, a % b)


a = 1071
b = 462

gcd_value, iterations = gcd_iterative(a, b)
recursive_value = gcd_recursive(a, b)

print("Numbers:", a, b)
print("GCD using iterative method:", gcd_value)
print("Euclid iterations:", iterations)
print("GCD using recursive method:", recursive_value)
