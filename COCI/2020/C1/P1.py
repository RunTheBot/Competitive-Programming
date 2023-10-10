# COCI 2020 Contest 1 Problem 1
# DMOJ: https://dmoj.ca/problem/coci20c1p1

class Direction:
    North = (0, -1)
    South = (0, 1)
    East = (1, 0)
    West = (-1, 0)

def addCoord(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])


def BFS(start, mazeSize, maze):
    mazeX, mazeY = mazeSize
    visited = [[False for i in range(mazeX)] for j in range(mazeY)]

    try:
        if maze[start[1]][start[0]] == ".":
            return False
    except IndexError:
        pass

    queue = [start]
    count = 1
    while len(queue) > 0:
        try:
            current = queue.pop(0)
            currentVal = maze[current[1]][current[0]]
            if currentVal == "x":
                return count
            if currentVal == "o":
                return False

            nextPose = (0, 0)
            if currentVal == "^":
                nextPose = addCoord(current, Direction.North)
            if currentVal == "v":
                nextPose = addCoord(current, Direction.South)
            if currentVal == ">":
                nextPose = addCoord(current, Direction.East)
            if currentVal == "<":
                nextPose = addCoord(current, Direction.West)

            # print(f"nextPose: {nextPose} current: {current} currentVal: {currentVal} visited: {visited[nextPose[0]][nextPose[1]]} nextPoseVal: {maze[nextPose[1]][nextPose[0]]}")
            # print(f"mazeBool: {not maze[nextPose[1]][nextPose[0]] == '.'} visitedBool: {not visited[nextPose[1]][nextPose[0]]}")
            if not maze[nextPose[1]][nextPose[0]] == "." and not visited[nextPose[1]][nextPose[0]]:
                count += 1
                visited[nextPose[1]][nextPose[0]] = True
                queue.append(nextPose)
        except IndexError:
            continue
    return False

mazeY, mazeX = list(map(int, input().split()))

maze = [["." for i in range(mazeX)] for j in range(mazeY)]

start = (0, 0)

for y in range(mazeY):
    row = list(input())
    maze[y] = row
    for x in range(mazeX):
        if row[x] == "o":
            start = (x, y)

distances = []
distances.append(BFS(addCoord(start, Direction.East), (mazeX, mazeY), maze))
distances.append(BFS(addCoord(start, Direction.North), (mazeX, mazeY), maze))
distances.append(BFS(addCoord(start, Direction.South), (mazeX, mazeY), maze))
distances.append(BFS(addCoord(start, Direction.West), (mazeX, mazeY), maze))

# find the shortest distance
shortest = 1000000
shortestIndex = -1
for distance in range(len(distances)):
    # print(distances[distance])
    if distances[distance] and distances[distance] < shortest:
        shortest = distances[distance]
        shortestIndex = distance

# print(distances)
# print(shortestIndex)

# print shortest direction

if shortestIndex == -1:
    print(":(")
else:
    print(":)")
    if shortestIndex == 1:
        print("N")
    elif shortestIndex == 2:
        print("S")
    elif shortestIndex == 0:
        print("E")
    elif shortestIndex == 3:
        print("W")
