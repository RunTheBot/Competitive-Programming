import re

for i in range(int(input())):
     print(re.sub(r"\b\S{4}\b", "****", input()))
