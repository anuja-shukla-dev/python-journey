import re

pattern = r"\d+"
text = "I have 2 cats, 15 books and 300 rupees."

match = re.findall(pattern,text)
print(match)