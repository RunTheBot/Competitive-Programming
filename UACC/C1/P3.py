# The goal is to find that max ammount of capturable pieces in checkers by using DFS
# it is player A's turn

# Example Input
# ........
# ........
# .B.B.B..
# ........
# .B.B.B..
# ........
# .B.B.B..
# ..A.....

# Example Output
# 7

# Find max ammount of capturable pieces in checkers by using DFS
def DFS(start, board, captures):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    maxCaptures = 0

    hasCaptures = False
    for direction in directions:
        copy = [row.copy() for row in board]
        nextPose = (start[0] + direction[0], start[1] + direction[1])
        if nextPose[0] >= 0 and nextPose[0] < 8 and nextPose[1] >= 0 and nextPose[1] < 8:
            if copy[nextPose[0]][nextPose[1]] == 'B':
                hoppedPose = (nextPose[0] + direction[0], nextPose[1] + direction[1])
                if hoppedPose[0] >= 0 and hoppedPose[0] < 8 and hoppedPose[1] >= 0 and hoppedPose[1] < 8:
                    if copy[hoppedPose[0]][hoppedPose[1]] == '.':
                        copy[nextPose[0]][nextPose[1]] = '.' # remove the piece
                        maxCaptures = max(maxCaptures, DFS(nextPose, copy, captures + 1))
                        hasCaptures = True

    if not hasCaptures:
        return captures


    return maxCaptures

# Input
board = []
for i in range(8):
    board.append(list(input()))

# Loop through the board and find all the A's and start a search from there

maxCaptures = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == 'A':
            maxCaptures = max(maxCaptures, DFS((i, j), board, 0))

print(maxCaptures)



