# Graph Contest 3 P1 - Travelling Salesmen
# DMOJ: https://dmoj.ca/problem/graph3p1

def BFS(startQueue, graph, visited):
    queue = startQueue
    time = 0
    while len(queue) > 0:
        current, moves = queue.pop(0)
        for next in graph[current]:
            if not visited[next]:
                visited[next] = True
                time = moves + 1
                queue.append((next, moves + 1))
    return time

cities, roads = map(int, input().split())

graph = [[] for i in range(cities)]

for i in range(roads):
    start, end = map(int, input().split())
    graph[start-1].append(end-1)
    graph[end-1].append(start-1)

visited = [False for i in range(cities)]

startQueue = []

for j in range(int(input())):
    start = int(input())
    startQueue.append((start-1, 0))
    visited[start-1] = True

print(BFS(startQueue, graph, visited))

# for i in range(cities):
#     for j in range(len(graph[i])):
#         print(i, end=" ")
#         print(graph[i][j])
