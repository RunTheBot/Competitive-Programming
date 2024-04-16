# A Noisy Class
# DMOJ: https://dmoj.ca/problem/anoisyclass
import sys

# Input:
# 4
# 4
# 1 2
# 2 3
# 2 4
# 4 3

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# print(graph)

# def dfs(node):
#     visited.add(node)
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             dfs(neighbor)
#     result.append(node)

visited = set()
currently_exploring = set()

def dfs(node):
    visited.add(node)
    currently_exploring.add(node)

    for neighbor in graph[node]:
        if neighbor in currently_exploring:
            return True  # Cycle detected
        if neighbor not in visited:
            if dfs(neighbor):
                return True

    currently_exploring.remove(node)
    return False

for node in range(1, N+1):
    if node not in visited:
        if dfs(node):
            print("N")
            sys.exit()

print("Y")