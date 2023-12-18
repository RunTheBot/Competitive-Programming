# MWC 2015 #4 P4: Dealing with Knots
# DMOJ: https://dmoj.ca/problem/mwc15c4p4

def BFS(graph, start, end):
    visited = [False for i in range(N)]
    queue = [start]
    while len(queue) > 0:
        try:
            current = queue.pop(0)
            if current == end:
                return True
            adjacents = graph[current]
            for adjacent in adjacents:
                if not visited[adjacent]:
                    visited[adjacent] = True
                    queue.append(adjacent)
        except IndexError:
            continue
    return False


N = int(input())
graph = [[] for i in range(N+1)]

for i in range(N):
    knotA, knotB = list(map(int, input().split()))
    graph[knotA].append(knotB)

x, y = list(map(int, input().split()))

if BFS(graph, x, y):
    print("Tangled")
else:
    print("Not Tangled")
