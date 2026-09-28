
# Q21: String Formatting - Mark Sheet Header

name = "Sona Kumari"
roll = "2626299"
percentage = 87.50

width = 46
border = "+" + "-" * width + "+"

print(border)
print("|" + "VIDYA ANALYTICS".center(width) + "|")
print("|" + "Student Mark Sheet".center(width) + "|")
print(border)

# 1. % formatting
header_percent = "|%-20s%12s%10.2f%%|" % (name, roll, percentage)
print(header_percent)

# 2. str.format()
header_format = "|{:<20}{:^12}{:>10.2f}%|".format(
    name, roll, percentage
)
print(header_format)

# 3. f-string
header_fstring = f"|{name:<20}{roll:^12}{percentage:>10.2f}%|"
print(header_fstring)

print(border)

print("\nF-string format used:")
print(f"{name:<20}{roll:^12}{percentage:>8.2f}%")
