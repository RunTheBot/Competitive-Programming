def min_moves(surface_dim, num_cubes, cubes):
    surface = [[0] * surface_dim[1] for _ in range(surface_dim[0])]

    for r, c in cubes:
        surface[r - 1][c - 1] += 1

    min_row = min([r - 1 for r, _ in cubes])
    max_row = max([r - 1 for r, _ in cubes])
    min_col = min([c - 1 for _, c in cubes])
    max_col = max([c - 1 for _, c in cubes])

    moves = (max_row - min_row + 1) * (max_col - min_col + 1) - num_cubes

    return moves

# Read input
surface_dim = tuple(map(int, input().split()))
num_cubes = surface_dim[1]
cubes = [tuple(map(int, input().split())) for _ in range(num_cubes)]

# Calculate and print the result
result = min_moves(surface_dim, num_cubes, cubes)
print(result)
