from sys import stdin
import sys
prev = ""
out = []
for i in range(int(stdin.readline())):
    curr = stdin.readline().lower()
    if "yubo" in curr:
        out.append(curr)
        if prev != "":
            out.append(prev)
    prev = curr

for i in sorted(set(out)):
    sys.stdout.write(i)
