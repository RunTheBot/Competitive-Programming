# Problem: DWITE '10 R1 #5 - Ricochet Robot
# DMOJ: https://dmoj.ca/problem/dwite10c1p5

import sys
input = (lambda: sys.stdin.readline().strip())

graph = [ ["#" for _ in range(12)] for _ in range(12)]

startPos = None
endPos = None

for y in range(1,11):
    print()
    line = input()
    for x in range(1,11):
        graph[y][x] = line[x-1]
        if line[x-1] == "A":
            startPos = (x,y)
        elif line[x-1] == "B":
            endPos = (x,y)
    

for row in graph:
    print("".join(row))

print(f'\n{startPos} {endPos}')
