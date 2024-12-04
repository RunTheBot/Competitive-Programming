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
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

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
        corner1, corner2 = corners[k], corners[(k+1) % ep]
        if corner1 > corner2:
            corner1, corner2 = corner2, corner1
        if (corner1, corner2) in fence:
            x, co, outside = fence[(corner1, corner2)]
            edges.append((costs[k], i, x))
            fence[(corner1, corner2)] = (i, costs[k], False) 
        else:
            fence[(corner1, corner2)] = (i, costs[k], True)  

outside_edges = []
for (corner1, corner2), (pen, cost, is_outside) in fence.items():
    if is_outside:
        outside_edges.append((cost, pen, M))

internal_cost = kruskal(edges, M)
with_outside_cost = kruskal(edges + outside_edges, M + 1)

print(min(internal_cost, with_outside_cost))
