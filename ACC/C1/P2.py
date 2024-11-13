# Another Contest 1 Problem 2 - Graphs
# DMOJ: https://dmoj.ca/problem/acc1p2

from collections import deque, defaultdict

# Union-Find (Disjoint Set Union) Implementation
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def bidirectional_bfs(graph, start, end):
    if start == end:
        return 0

    queue_start = deque([(start, 0)])
    queue_end = deque([(end, 0)])
    visited_start = {start: 0}
    visited_end = {end: 0}

    while queue_start and queue_end:
        node, dist = queue_start.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited_start:
                visited_start[neighbor] = dist + 1
                queue_start.append((neighbor, dist + 1))
                if neighbor in visited_end:
                    return dist + 1 + visited_end[neighbor]

        node, dist = queue_end.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited_end:
                visited_end[neighbor] = dist + 1
                queue_end.append((neighbor, dist + 1))
                if neighbor in visited_start:
                    return dist + 1 + visited_start[neighbor]

    return -1

N, M, Q = map(int, input().split())
graph = defaultdict(list)

uf = UnionFind(N)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    uf.union(u - 1, v - 1) 

for _ in range(Q):
    a, b = map(int, input().split())
    if uf.find(a - 1) != uf.find(b - 1):
        print(-1)
    else:
        print(bidirectional_bfs(graph, a, b))
