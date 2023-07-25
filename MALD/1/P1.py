from sys import stdin
import sys
prev = ""
donext = False
out = []
for i in range(int(stdin.readline())):
    curr = stdin.readline()
    if donext:
        out.append(curr)
        donext = False
    if "yubo" in curr:
        out.append(curr)
        if prev != "":
            out.append(prev)
        donext = True
    prev = curr

for i in sorted(set(out)):
    sys.stdout.write(i)
