import re

pattern = r"\s+"
text = "Hello     World     Python"

match = re.sub(pattern," ",text)
print(match)