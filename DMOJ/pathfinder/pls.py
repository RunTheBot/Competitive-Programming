# Pathfinder
# DMOJ: https://www.dmoj.ca/problem/pathfind
from enum import Enum


# Enum for north, south, east, west
class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

n, m, k = map(int, input().split())

walls = set()
visited = set()
edgeWalls = []

for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    walls.add((x, y))
    if x == 0 or x == n-1 or y == 0 or y == m-1:
        edgeWalls.append((x, y))

def print_grid(grid):
    for i in range(n):
        for j in range(m):
            if (i, j) in grid:
                print("#", end="")
                # grid[i][j] = "#"
            else:
                print(".", end="")
        print()



# print_grid(walls)

def print_path(path):
    print(path)
    for i in range(n):
        for j in range(m):
            if (i, j) in path:
                print("#", end="")
            else:
                print(".", end="")
        print()

def BFS(start, endEdgeType):
    queue = [start]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    path = [start]
    while queue:
        current = queue.pop(0)
        # if a different edge of the grid is reached, then we have found a path
        path.append(current)
        visited.add(current)
        for direction in directions:
            x, y = current
            x += direction[0]
            y += direction[1]
            if (x, y) in walls and (x, y) not in visited:
                queue.append((x, y))
    return False

for wall, endEdgeType in edgeWalls:
    if wall in visited:
        continue
    visited.add(wall)
    # print("Checking if there is a path from", wall, "to", endEdgeType, "With Type", getEdgeType(wall))
    # print the row
    # print("Row", [wall[0]])
    if BFS(wall, endEdgeType):
        print("NO")
        break
else:
    print("YES")
