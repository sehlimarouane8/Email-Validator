import re

email = input("Enter an email address: ")

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid email address ✅")
else:
    print("Invalid email address ❌")
