import re

email = input("Enter email: ")

pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.match(pattern, email):
    print("Valid")
else:
    print("Invalid")

