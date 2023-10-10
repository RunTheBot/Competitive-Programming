

def BFS(start, end, mazeSize, maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = [start]
    visited = [[False for i in range(mazeSize[1])] for j in range(mazeSize[0])]

    while len(queue) > 0:
        current = queue.pop(0)
        for direction in directions:
            if current == end:
                return True
            nextPose = (current[0] + direction[0], current[1] + direction[1])
            if maze[nextPose[0]][nextPose[1]] == 0 and not visited[nextPose[0]][nextPose[1]]:
                visited[nextPose[0]][nextPose[1]] = True
                queue.append(nextPose)
    return False
