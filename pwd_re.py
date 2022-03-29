import re

password = "A@vasantham6228"

pattern = "(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^a-zA-Z0-9])(?=.{8})"

if (re.search(pattern, password)):
    print("Valid Password Entry")
else:
    print("Invalid")