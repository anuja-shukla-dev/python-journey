import re

pattern = r"\d+"
text = "A1 B2 C3 D4"

matches = re.findall(pattern,text)
count = 0
for match in matches:
    count+=1

print(count)