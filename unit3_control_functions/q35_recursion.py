
"""
Q35: Recursion

Demonstrates:
1. Recursive factorial
2. Recursive Fibonacci
3. Recursive sum of digits
4. Recursive string reversal
5. Recursive GCD
6. Recursive vs iterative Fibonacci runtime
7. RecursionError
"""


# 1. Recursive Factorial
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


# 2. Recursive Fibonacci
def fibonacci_recursive(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# 3. Recursive Sum of Digits
def sum_digits(n):
    # Base case
    if n == 0:
        return 0

    # Recursive case
    return (n % 10) + sum_digits(n // 10)


# 4. Recursive String Reverse
def reverse_string(text):
    # Base case
    if len(text) <= 1:
        return text

    # Recursive case
    return text[-1] + reverse_string(text[:-1])


# 5. Recursive GCD
def gcd_recursive(a, b):
    # Base case
    if b == 0:
        return abs(a)

    # Recursive case
    return gcd_recursive(b, a % b)


# 6. Iterative Fibonacci
def fibonacci_iterative(n):
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a


# Test values
print("===== RECURSIVE FACTORIAL =====")
print("Factorial of 5:", factorial(5))


print("\n===== RECURSIVE FIBONACCI =====")
print("Fibonacci(10):", fibonacci_recursive(10))


print("\n===== SUM OF DIGITS =====")
roll_number = 2626299
print("Roll Number:", roll_number)
print("Sum of digits:", sum_digits(roll_number))


print("\n===== REVERSE STRING =====")
text = "VIDYA"
print("Original:", text)
print("Reversed:", reverse_string(text))


print("\n===== RECURSIVE GCD =====")
print("GCD of 48 and 18:", gcd_recursive(48, 18))


# 7. Runtime comparison for n = 30
import time

n = 30

start = time.time()
recursive_result = fibonacci_recursive(n)
recursive_time = time.time() - start

start = time.time()
iterative_result = fibonacci_iterative(n)
iterative_time = time.time() - start

print("\n===== FIBONACCI RUNTIME COMPARISON =====")
print("n:", n)
print("Recursive Fibonacci:", recursive_result)
print("Recursive time:", recursive_time, "seconds")
print("Iterative Fibonacci:", iterative_result)
print("Iterative time:", iterative_time, "seconds")


# 8. Trigger RecursionError
print("\n===== RECURSION ERROR DEMONSTRATION =====")


def infinite_recursion(n):
    return infinite_recursion(n + 1)


try:
    infinite_recursion(1)
except RecursionError:
    print("RecursionError: maximum recursion depth exceeded.")
    print("Explanation: The function keeps calling itself without a base case.")
