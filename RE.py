import re
string = "FLIFO#CM100/SFO/PTYEA"
mail = "mdharwin91@gmail.com"

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#pattern = "[EA$]"
if (re.fullmatch(regex, mail)):
    print("Valid")
else:
    print("Invalid")


