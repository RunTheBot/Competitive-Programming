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

best = {}
second_best = {}
count = {}
for P, C in pens:
    if C not in best:
        best[C] = P
        second_best[C] = -10**9
        count[C] = 1
    else:
        if P > best[C]:
            second_best[C] = best[C]
            best[C] = P
            count[C] = 1
        elif P == best[C]:
            count[C] += 1
        else:
            second_best[C] = max(second_best[C], P)

base_score = sum(best.values())
missing = M - len(best)

max_improve = 0
if missing > 0:
    for P, C in pens:
        if not (P == best[C] and count[C] == 1):
            max_improve = max(max_improve, P)
else:
    best_items = list(best.items()) 
    best_items.sort(key=lambda x: x[1])
    global_min = best_items[0][1]
    global_min_count = sum(1 for c, v in best_items if v == global_min)
    second_global_min = best_items[1][1] if len(best_items) > 1 else global_min

    for P, C in pens:
        if best[C] == global_min and global_min_count == 1:
            target = second_global_min
        else:
            target = global_min
        if P <= target:
            continue 
        if not (P == best[C] and count[C] == 1):
            gain = P - target
        else:
            gain = P - target - (best[C] - second_best[C])
        max_improve = max(max_improve, gain)

ans = base_score + max_improve
print(ans)








