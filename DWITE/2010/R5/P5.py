# Problem: DWITE '10 R1 #5 - Ricochet Robot
# DMOJ: https://dmoj.ca/problem/dwite10c1p5

import sys

input = (lambda: sys.stdin.readline().strip())

direction = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}


def addCoord(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def getVal(coord, graph):
    return graph[coord[1]][coord[0]]


def BFS(startPos, endPos, graph):
    # Pos, Number of moves
    queue = []
    visited = [[False for _ in range(12)] for _ in range(12)]

    for currDir in direction:
        queue.append([addCoord(startPos, direction[currDir]), 1, currDir])

    for queueItem in queue:
        current = queue.pop(0)
        pos, moves, currDir = current
        nextPose = addCoord(pos, direction[currDir])
        prevPose = pos
        while getVal(nextPose, graph) != "#":
            prevPose = nextPose
            nextPose = addCoord(nextPose, direction[currDir])
        queue.append([prevPose, moves])
        visited[prevPose[1]][prevPose[0]] = True

    while len(queue) > 0:
        pos, moves = queue.pop(0)
        visited[pos[1]][pos[0]] = True
        if pos == endPos:
            return moves
        for newDir in direction:
            nextPose = addCoord(pos, direction[currDir])
            prevPose = pos
            while getVal(nextPose, graph) != "#":
                prevPose = nextPose
                nextPose = addCoord(nextPose, direction[currDir])
            if not visited[prevPose[1]][prevPose[0]]:
                queue.append([prevPose, moves + 1])
    return False


graph = [["#" for _ in range(12)] for _ in range(12)]

startPos = None
endPos = None

for y in range(1, 11):
    print()
    line = input()
    for x in range(1, 11):
        graph[y][x] = line[x - 1]
        if line[x - 1] == "A":
            startPos = (x, y)
        elif line[x - 1] == "B":
            endPos = (x, y )

for row in graph:
    print("".join(row))

print(f'\n{startPos} {endPos}')

print(BFS(startPos, endPos, graph))
