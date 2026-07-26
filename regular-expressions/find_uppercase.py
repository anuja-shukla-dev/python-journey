import re

pattern = r"\b[A-Z][A-Za-z]*\b"
text = "Anuja studies Python at CSJMU University."

match = re.findall(pattern,text)
print(match)