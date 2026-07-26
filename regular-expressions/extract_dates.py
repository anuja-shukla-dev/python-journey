import re

pattern = r"\d{2}-\d{2}-\d{4}"
text = "Exam on 24-07-2026 and interview on 30-08-2026."

match = re.findall(pattern,text)
print(match)