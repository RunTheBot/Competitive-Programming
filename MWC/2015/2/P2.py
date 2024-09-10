# MWC '15 #2 P2: Towering Towers
# DMOJ: https://dmoj.ca/problem/mwc15c2p2/

import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

visible_counts = [0] * n
stack = []

for i in range(n):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()
    if stack:
        visible_counts[i] = i - stack[-1]
    else:
        visible_counts[i] = i
    stack.append(i)

print(" ".join(map(str, visible_counts)))
