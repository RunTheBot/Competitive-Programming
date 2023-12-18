# DMOJ: https://dmoj.ca/problem/avocadotrees
# Avocado Trees!

input = __import__('sys').stdin.readline

n, q, h = map(int, input().split())
tree_heights = [0] * n
avocado_yield = [0] * n

for i in range(n):
    height, yield_ = map(int, input().split())
    tree_heights[i] = height
    avocado_yield[i] = yield_

max_avocados = 0

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1  # Adjust to 0-based indexing
    r -= 1  # Adjust to 0-based indexing

    max_avocados_range = 0
    for i in range(l, r + 1):
        if tree_heights[i] <= h:
            max_avocados_range += avocado_yield[i]

    max_avocados = max(max_avocados, max_avocados_range)

print(max_avocados)

