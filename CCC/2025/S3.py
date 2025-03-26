"""
6 3 0
1 6
2 9
3 4
2 7
3 9
1 3
"""

import sys


input = sys.stdin.readline

N, M, Q = map(int, input().split())

pens = []

for i in range(N):
    C, P = map(int, input().split())
    pens.append((P, C))

pens.sort()
pens.reverse()

seen = set()
swapped = False

max_score = 0

# print(pens)

i = 0
while i < M:
    P, C = pens[i]
    if C in seen:
        if not swapped:
            swapped = True
            max_score += P
            i += 1
    else:
        seen.add(C)
        max_score += P
        i += 1

print(max_score)
        


        




