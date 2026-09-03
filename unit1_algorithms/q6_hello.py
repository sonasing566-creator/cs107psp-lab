
from datetime import date
import subprocess

name = "Sona Kumari"
roll_no = "2626299"

branch = subprocess.check_output(
    ["git", "branch", "--show-current"],
    text=True
).strip()

today = date.today()

print("Name:", name)
print("Roll No.:", roll_no)
print("Branch:", branch)
print("Today's Date:", today)
