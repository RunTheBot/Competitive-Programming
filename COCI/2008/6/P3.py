# COCI '08 Contest 6 #3 Nered
# DMOJ: https://dmoj.ca/problem/coci08c6p3
# Approach: Prefix Sum Array


n, m = map(int, input().split())
grid = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
PSA = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# Input
for _ in range(m):
    r, c = map(int, input().split())
    grid[r][c] = 1

# print(grid)

# Prefix Sum Array
for r in range(1, n + 1):
    for c in range(1, n + 1):
        PSA[r][c] = PSA[r][c - 1] + PSA[r - 1][c] - PSA[r - 1][c - 1] + grid[r][c]

rectangles = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j == m:
            rectangles.append((i, j))

areaMax = 0
for h, w in rectangles:
    for r1 in range(1, n + 1 - h + 1):
        for c1 in range(1, n + 1 - w + 1):
            r2, c2 = r1 + h - 1, c1 + w - 1
            area = PSA[r2][c2] - PSA[r2][c1 - 1] - PSA[r1 - 1][c2] + PSA[r1 - 1][c1 - 1]
            areaMax = max(areaMax, area)

print(areaMax)
