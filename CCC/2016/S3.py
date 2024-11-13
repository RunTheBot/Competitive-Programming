# CCC '16 S3 - Phonomenal Reviews
# DMOJ: https://dmoj.ca/problem/ccc16s3

from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10**6)

def bfs(graph, start, n):
    dist = [-1] * n
    dist[start] = 0
    queue = deque([start])
    furthest = start
    
    while queue:
        curr = queue.popleft()
        for next_node in graph[curr]:
            if dist[next_node] == -1:
                dist[next_node] = dist[curr] + 1
                queue.append(next_node)
                if dist[next_node] > dist[furthest]:
                    furthest = next_node
    
    return furthest, dist[furthest]

N, M = map(int, input().split())
pho = set(map(int, input().split()))
graph = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N
important = set()

def dfs(node, parent):
    visited[node] = True
    is_important = node in pho
    
    for next_node in graph[node]:
        if next_node != parent and not visited[next_node]:
            if dfs(next_node, node):
                is_important = True
    
    if is_important:
        important.add(node)
    return is_important

start = next(iter(pho))
dfs(start, -1)

trimmed = defaultdict(list)
for v in important:
    for u in graph[v]:
        if u in important:
            trimmed[v].append(u)

end1, _ = bfs(trimmed, start, N)
end2, diameter = bfs(trimmed, end1, N)

total_edges = len(important) - 1
result = 2 * total_edges - diameter

print(result)
