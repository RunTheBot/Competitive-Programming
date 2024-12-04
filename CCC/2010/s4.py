class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

def kruskal(edges, n):
    uf = UnionFind(n)
    edges.sort()  
    total_cost = 0
    for cost, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            total_cost += cost
    
    root = uf.find(0)
    return total_cost if all(uf.find(i) == root for i in range(n)) else float('inf')

M = int(input())
fence = {}  
edges = []  

for i in range(M):
    wd = list(map(int, input().split()))
    ep = wd[0]
    corners = wd[1:1+ep]
    costs = wd[1+ep:]
    
    for k in range(ep):
        a, b = corners[k], corners[(k+1) % ep]
        if a > b:
            a, b = b, a
        if (a, b) in fence:
            x, co, outside = fence[(a, b)]
            edges.append((costs[k], i, x))
            fence[(a, b)] = (i, costs[k], False) 
        else:
            fence[(a, b)] = (i, costs[k], True)  

outside_edges = []
for (a, b), (pen, cost, is_outside) in fence.items():
    if is_outside:
        outside_edges.append((cost, pen, M))

internal_cost = kruskal(edges, M)
with_outside_cost = kruskal(edges + outside_edges, M + 1)

print(min(internal_cost, with_outside_cost))
