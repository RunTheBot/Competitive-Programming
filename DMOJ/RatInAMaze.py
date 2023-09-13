# Rat In A Maze
# DMOJ: https://dmoj.ca/problem/ccc00s3
# Algorithm: BFS

import sys
input = sys.stdin.readline

# Input Specification
N = int(input())
maze = [[1 for i in range(N+2)] for j in range(N+2)]

for i in range(1, N+1):
    maze[i] = [1] + list(map(int, input().split())) + [1]

# for row in maze:
#     print(" ".join(map(str, row)))

# BFS
start = (1, 1)
end = (N, N)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = [start]
visited = [[False for i in range(N+2)] for j in range(N+2)]

while len(queue) > 0:
    current = queue.pop(0)
    for direction in directions:
        if current == end:
            print("yes")
            sys.exit()
        next = (current[0] + direction[0], current[1] + direction[1])
        if maze[next[0]][next[1]] == 0 and not visited[next[0]][next[1]]:
            visited[next[0]][next[1]] = True
            queue.append(next)

print("no")
