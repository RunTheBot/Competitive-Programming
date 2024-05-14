# Baltic OI '04 P1 - Ships
# DMOJ: https://dmoj.ca/problem/btoi04p1

# The board of "Ships" game consists of N × N squares. Each square may belong to some ship or be empty. If two squares belong to ships and have a common edge, then both squares belong to the same ship. Squares of different ships have no common points. The tonnage of a ship is the number of squares belonging to this ship.
#
# In the given example, squares belonging to ships are marked black. On the game board there are: one 29 -ton ship, three 7 -ton ships, two 4 -ton ships and three one-ton ships.
#
# Write a program which for given description of a game board calculates number of ships and tonnage of each ship.

# The first line of input contains one positive integer N .
#
# On each of the next N lines, there is given information about one board row, consecutively describing groups of squares from left to right, which belongs to ships in one of two formats:
#
#     <number_of_square_column>, if square in given column belongs to ship, but squares to the left and to the right are free;
#     <number_of_first_square_column>-<number_of_last_square_column>, if all consecutive squares from first to last (including) belong to ship and squares to the left and to the right from this group are free.
#
# Square groups are separated by commas, each line ends with a semicolon. There are no spaces in lines. If in some board row there are no ship's squares, then the corresponding line contains only one semicolon.



n = int(input())
board = []

for _ in range(n):
    row = input().rstrip(";").split(",")
    row_values = ["0"] * n
    for group in row:
        if group:  # Check if group is not an empty string
            if "-" in group:
                start, end = map(int, group.split("-"))
                for i in range(start - 1, end):
                    row_values[i] = "1"
            else:
                row_values[int(group) - 1] = "1"
    board.append(row_values)


n = len(board)
ships = {}
visited = [[False for _ in range(n)] for _ in range(n)]

def bfs(row, col):
    tonnage = 0
    queue = [(row, col)]
    visited[row][col] = True

    while queue:
        r, c = queue.pop(0)
        tonnage += 1

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_r, new_c = r + dr, c + dc
            if (
                    0 <= new_r < n
                    and 0 <= new_c < n
                    and board[new_r][new_c] == "1"
                    and not visited[new_r][new_c]
            ):
                visited[new_r][new_c] = True
                queue.append((new_r, new_c))

    return tonnage

for i in range(n):
    for j in range(n):
        if board[i][j] == "1" and not visited[i][j]:
            tonnage = bfs(i, j)
            ships[tonnage] = ships.get(tonnage, 0) + 1

sorted_ships = sorted(ships.items(), reverse=True)

for tonnage, count in sorted_ships:
    print(tonnage, count)
