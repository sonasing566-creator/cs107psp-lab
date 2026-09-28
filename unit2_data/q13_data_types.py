import sys

a_int = 100
a_float = 25.5
a_complex = 3 + 4j
a_bool = True
a_str = "Vidya Analytics"
a_none = None

variables = [
    ("int", a_int),
    ("float", a_float),
    ("complex", a_complex),
    ("bool", a_bool),
    ("str", a_str),
    ("NoneType", a_none)
]

print("=" * 90)
print(f"{'Name':<12}{'Value':<20}{'type()':<25}{'id()':<20}{'Size':<10}")
print("=" * 90)

for name, value in variables:
    print(
        f"{name:<12}"
        f"{str(value):<20}"
        f"{str(type(value)):<25}"
        f"{id(value):<20}"
        f"{sys.getsizeof(value):<10}"
    )

print("=" * 90)

# Bonus: Integer caching
a = 100
b = 100

print("\nInteger Caching:")
print("a = 100, b = 100")
print("id(a) == id(b):", id(a) == id(b))

a = 1000
b = 1000

print("\na = 1000, b = 1000")
print("id(a) == id(b):", id(a) == id(b))
