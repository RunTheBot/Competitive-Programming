def count_safe_tiles(n, w, h, lasers):
    # Initialize the room with all tiles as safe
    room = [[1 for _ in range(w)] for _ in range(h)]

    # For each laser
    for laser in lasers:
        x1, y1, x2, y2 = laser

        # If the laser is vertical
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                room[y][x1] = 0
        # If the laser is horizontal
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                room[y1][x] = 0
        # If the laser is diagonal
        else:
            for x, y in zip(range(x1, x2, 1 if x1 < x2 else -1), range(y1, y2, 1 if y1 < y2 else -1)):
                room[y][x] = 0

    # Count the number of safe tiles
    safe_tiles = sum(row.count(1) for row in room)

    return safe_tiles

x, y, z = map(int, input().split())
print(count_safe_tiles(x, y, z, [list(map(int, input().split())) for _ in range(x)])-1)