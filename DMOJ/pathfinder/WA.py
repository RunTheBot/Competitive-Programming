from enum import Enum
from collections import deque

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
    wallType = getEdgeType(wall)
    endWallType = set()
    if Direction.NORTH in wallType:
        endWallType.add(Direction.WEST)
        endWallType.add(Direction.SOUTH)
    if Direction.SOUTH in wallType:
        endWallType.add(Direction.EAST)
        endWallType.add(Direction.NORTH)
    if Direction.EAST in wallType:
        endWallType.add(Direction.SOUTH)
        endWallType.add(Direction.WEST)
    if Direction.WEST in wallType:
        endWallType.add(Direction.NORTH)
        endWallType.add(Direction.EAST)
    return endWallType

edgeWalls = [(wall, getEndEdgeType(wall)) for wall in walls if wall[0] in {0, n-1} or wall[1] in {0, m-1}]

def BFS(start, endEdgeType):
    queue = deque([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    while queue:
        current = queue.popleft()
        edgeType = getEdgeType(current)
        if not edgeType == set() and edgeType.issubset(endEdgeType):
            return True
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
    if wall in visited:
        continue
    if BFS(wall, endEdgeType):
        print("NO")
        break
else:
    print("YES")
