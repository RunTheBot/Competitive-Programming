# BFS Solution
# DMOPC '18 Contest 6 P3 - Wish Upon a Star

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

if M > N:
    print("NO")
    sys.exit()

adj = [[] for _ in range(N + 1)] 
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (N + 1)
loops = 0

for i in range(1, N + 1):
    if not visited[i]:
        loops += 1
        queue = deque()
        queue.append(i)
        visited[i] = True
        while queue:
            current_node = queue.popleft()
            for next_node in adj[current_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

concycle = M - N + loops
if concycle <= 1:
    print("YES")
else:
    print("NO")