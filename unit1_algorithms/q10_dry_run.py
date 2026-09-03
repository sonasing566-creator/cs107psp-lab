# (a) Swap using a temporary variable
a = 10
b = 20

temp = a
a = b
b = temp

print("Swap using temp:")
print("a =", a)
print("b =", b)


# (b) Swap without a temporary variable
x = 10
y = 20

x, y = y, x

print("Swap without temp:")
print("x =", x)
print("y =", y)


# (c) Factorial of 5 using iteration
n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial of 5:", fact)
