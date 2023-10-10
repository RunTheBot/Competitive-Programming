# DWITE '07 R5 #4 - Train ride
# DMOJ: https://dmoj.ca/problem/dwite07c5p4

def BFS(start, mazeSize, maze):
    # 8 directions
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, -1), (-1, 1), (1, 1)]
    queue = [(start, 0)]
    visited = [[False for i in range(mazeSize[1])] for j in range(mazeSize[0])]

    while len(queue) > 0:
        current, moves = queue.pop(0)
        if maze[current[0]][current[1]] == "E":
            return moves
        for direction in directions:
            nextPose = (current[0] + direction[0], current[1] + direction[1])
            try:
                if maze[nextPose[0]][nextPose[1]] != "x" and not visited[nextPose[0]][nextPose[1]]:
                    visited[nextPose[0]][nextPose[1]] = True
                    queue.append((nextPose, moves + 1))
            except:
                pass

    return -1

for _ in range(5):
    maze = []

    start = None

    while True:
        line = input()
        if line == "xxxxxxxxxx":
            break
        line = line.replace(" ", "x")
        # print(line)
        maze.append(["x"] + list(line.replace(" ", "x")) + ["x"])
        if start == None:
            for i in range(len(maze[-1])):
                if maze[-1][i] == "S":
                    start = (len(maze), i)

    maze.append(["x"]*12)
    maze.insert(0, ["x"]*12)
    #
    # for i in range(len(maze)):
    #     print("".join(maze[i]))
    #
    # print(maze[start[0]][start[1]])
    mazeSize = (len(maze)+2, 12)
    print(BFS(start, mazeSize, maze))

