from collections import deque

def get_edge_type(x, y, n, m):
    edge_type = set()
    if x == 0:
        edge_type.add((0, -1))  # North
    if x == n - 1:
        edge_type.add((0, 1))  # South
    if y == 0:
        edge_type.add((-1, 0))  # West
    if y == m - 1:
        edge_type.add((1, 0))  # East
    return edge_type

def bidirectional_bfs(start, end_edge_type, walls, n, m):
    queue_start = deque([start])
    queue_end = deque(end_edge_type)
    visited_start = set([start])
    visited_end = set(end_edge_type)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    while queue_start and queue_end:
        current_start = queue_start.popleft()
        for direction in directions:
            x, y = current_start
            x += direction[0]
            y += direction[1]
            if (x, y) in walls or (x, y) in visited_start:
                continue
            if (x, y) in visited_end:
                return True
            visited_start.add((x, y))
            queue_start.append((x, y))

        current_end = queue_end.popleft()
        for direction in directions:
            x, y = current_end
            x += direction[0]
            y += direction[1]
            if (x, y) in walls or (x, y) in visited_end:
                continue
            if (x, y) in visited_start:
                return True
            visited_end.add((x, y))
            queue_end.append((x, y))

    return False

n, m, k = map(int, input().split())
walls = set((x - 1, y - 1) for x, y in [map(int, input().split()) for _ in range(k)])

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if (i, j) not in walls:
            continue
        edge_type = get_edge_type(i, j, n, m)
        end_edge_type = set()
        for direction in edge_type:
            x, y = i, j
            x += direction[0]
            y += direction[1]
            if (x, y) in walls:
                continue
            end_edge_type.add((x, y))
        if end_edge_type:
            if bidirectional_bfs((i, j), end_edge_type, walls, n, m):
                print("NO")
                exit()

print("YES")
