import re

pattern = r"#\w+"
text = "Learning #Python #Regex #100DaysOfCode"

match = re.findall(pattern,text)
print(match)