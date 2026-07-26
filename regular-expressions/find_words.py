import re

pattern = r"\w+"
text = "Python is fun!"

match = re.findall(pattern,text)
print(match)