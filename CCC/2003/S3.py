# 2003 Canadian Computing Competition
# Senior Division
# Problem S3: Floor Plan
# DMOJ: https://dmoj.ca/problem/ccc03s3

import sys

input = sys.stdin.readline

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def BFS(graph, start, visited, wall):
    queue = [start]
    count = 0
    while len(queue) > 0:
        current = queue.pop(0)
        count += 1
        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])
            try:
                if not visited[next[0]][next[1]] and graph[next[0]][next[1]] != wall:
                    visited[next[0]][next[1]] = True
                    queue.append(next)
            except IndexError:
                continue
    return count




# Input
wood = int(input().strip())
rows = int(input().strip())
columns = int(input().strip())
rooms = [[0 for i in range(columns + 2)] for j in range(rows + 2)]

areas = []


wall = "I"

graph = [[wall for j in range(columns + 2)] for i in range(rows + 2)]
visited = [[False for j in range(columns + 2)] for i in range(rows + 2)]

for i in range(1, rows + 1):
    row = list(input().strip())
    graph[i] = [wall] + row + [wall]

for row in range(1, rows + 1):
    for column in range(1, columns + 1):
        if graph[row][column] == wall:
            continue
        if not visited[row][column]:
            visited[row][column] = True
            area = BFS(graph, (row, column), visited, wall)
            areas.append(area)

areas.sort(reverse=True)

roomCount = 0

for _ in range(len(areas)):
    area = areas.pop(0)
    # print(f'{wood}-{area}')
    if wood-area >= 0:
        wood -= area
        roomCount += 1
    else:
        break

if roomCount == 1:
    print(f'{roomCount} room, {wood} square metre(s) left over')
else:
    print(f'{roomCount} rooms, {wood} square metre(s) left over')
