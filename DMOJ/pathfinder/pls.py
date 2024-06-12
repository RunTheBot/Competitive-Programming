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

for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    walls.add((x, y))

# find all the walls that are on the edge of the grid, edges are defined as the
#  squares that are x = 0 or x = n-1 or y = 0 or y = m-1

def getEdgeType(wall):
    edgeType = set()
    if wall[0] == 0:
        edgeType.add(Direction.NORTH)
    if wall[0] == n-1:
        edgeType.add(Direction.SOUTH)
    if wall[1] == 0:
        edgeType.add(Direction.WEST)
    if wall[1] == m-1:
        edgeType.add(Direction.EAST)

    return edgeType


def getEndEdgeType(wall):
    # if there will be a complete line blocking the top right to bottom left
    #  The the bfs should end
    # for example a wall stating at SOUTH can end at north or east bur not west(does not form a blocking line) or south (It cannot form a blocking line)
    wallType = getEdgeType(wall)
    endWallType = set()
    if Direction.NORTH in wallType:
        endWallType.add(Direction.WEST)
        endWallType.add(Direction.SOUTH)
    if Direction.SOUTH in wallType:
        endWallType.add(Direction.EAST)
        endWallType.add(Direction.NORTH)
    if Direction.EAST in wallType:
        endWallType.add(Direction.NORTH)
        endWallType.add(Direction.WEST)
    if Direction.WEST in wallType:
        endWallType.add(Direction.SOUTH)
        endWallType.add(Direction.EAST)
    return endWallType


edgeWalls = []
for wall in walls:
    if wall[0] == 0 or wall[0] == n-1 or wall[1] == 0 or wall[1] == m-1:
        endEdgeType = getEndEdgeType(wall)
        edgeWalls.append((wall, endEdgeType))

# print the grid by building a string
# def print_grid(grid):
#     for i in range(n):
#         for j in range(m):
#             if (i, j) in grid:
#                 print("#", end="")
#             else:
#                 print(".", end="")
#         print()
#
# print_grid(walls)

def BFS(start, endEdgeType):
    queue = [start]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    while queue:
        current = queue.pop(0)
        # if a different edge of the grid is reached, then we have found a path
        edgeType = getEdgeType(current)
        if edgeType != set() and edgeType.issubset(endEdgeType):
            return False
        visited.add(current)
        for direction in directions:
            x, y = current
            x += direction[0]
            y += direction[1]
            if (x, y) in walls and (x, y) not in visited:
                queue.append((x, y))
    return True

for wall, edgeType in edgeWalls:
    visited.add(wall)
    # print("Checking if there is a path from", wall, "to", edgeType)
    if BFS(wall, edgeType):
        print("YES")
        break
else:
    print("NO")
