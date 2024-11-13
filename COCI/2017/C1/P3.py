from collections import deque

# Define the shapes of the Tetris figures and their rotations
SHAPES = [
    [[(0,0),(0,1),(0,2),(0,3)], [(0,0),(1,0),(2,0),(3,0)]],  # I
    [[(0,0),(0,1),(1,0),(1,1)]],  # O
    [[(0,0),(1,0),(2,0),(2,1)], [(0,0),(0,1),(0,2),(1,0)], [(0,0),(0,1),(1,1),(2,1)], [(0,2),(1,0),(1,1),(1,2)]],  # L
    [[(0,0),(1,0),(1,1),(2,1)], [(0,1),(0,2),(1,0),(1,1)]],  # Z
    [[(0,0),(0,1),(0,2),(1,1)], [(0,1),(1,0),(1,1),(2,1)], [(1,0),(1,1),(1,2),(0,1)], [(0,0),(1,0),(1,1),(2,0)]]  # T
]

def bfs(matrix, start, color):
    n, m = len(matrix), len(matrix[0])
    queue = deque([start])
    visited = set([start])
    shape = [start]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == color and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                shape.append((nx, ny))
    
    return shape

def normalize_shape(shape):
    min_x = min(x for x, y in shape)
    min_y = min(y for x, y in shape)
    return sorted((x - min_x, y - min_y) for x, y in shape)

def count_figures(matrix):
    n, m = len(matrix), len(matrix[0])
    visited = set()
    counts = [0] * 5

    for i in range(n):
        for j in range(m):
            if matrix[i][j] != '.' and (i, j) not in visited:
                shape = bfs(matrix, (i, j), matrix[i][j])
                visited.update(shape)
                normalized_shape = normalize_shape(shape)
                
                for fig_idx, rotations in enumerate(SHAPES):
                    if any(normalized_shape == normalize_shape(rotation) for rotation in rotations):
                        counts[fig_idx] += 1
                        break

    return counts

# Read input
n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

# Count figures and print results
results = count_figures(matrix)
for count in results:
    print(count)