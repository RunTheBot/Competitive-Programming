# DWITE '07 R5 #5 - Tetris!

""" DWITE Online Computer Programming Contest, February 2008, Problem 5
You are working on a part of Tetris! playing AI that figures out the best move for the current piece, and one part of the information required for this decision is knowing the maximum number of lines that the current piece can score on a given board.

The board size is 
10
 units in width, and 6 in height. A line is complete when all 
10
 units across are filled with a game piece. It is made up of 2 possible characters:

# - piece on a board
. - empty spot
Pieces in play are standard Tetris piesces, and the current game piece will be described in a 
4
 by 
4
 matrix, at the beginning of each data set. The pieces can rotate, and thus can be presented in any orientation. Same character map as the board applies. For example:

Copy
....
.##.
##..
....
The input will come in 5 sets, repeating the following pattern: 
4
 lines, 
4
 characters each, describing the current piece in play. Followed by 6 lines, 10 characters each, describing the current board.

The output will contain 5 lines – a maximum number of lines that a piece can score.

Note: The piece starts dropping from above the supplied 
6
×
10
 board, and cannot be moved sideways during the fall. That is, you need to concern yourself only with the vertical drop.

Sample Input
Copy
....
.#..
.###
....
..........
..........
..........
#####..###
##.##.####
#####.####
Sample Output
Copy
2
 """


def can_place(board, piece, x, y):
    for i in range(4):
        for j in range(4):
            if piece[i][j] == '#' and (x + i >= 6 or board[x + i][y + j] == '#'):
                return False
    return True

def place_piece(board, piece, x, y):
    new_board = [list(row) for row in board]
    for i in range(4):
        for j in range(4):
            if piece[i][j] == '#':
                new_board[x + i][y + j] = '#'
    return [''.join(row) for row in new_board]


piece = []
board = []
for i in range(4):
    piece.append(input())
for i in range(6):
    board.append(input())
max_lines = 0
for _ in range(4):
    for y in range(7):
        for x in range(3, -1, -1):
            if can_place(board, piece, x, y):
                new_board = place_piece(board, piece, x, y)
                max_lines = max(max_lines, sum(1 for row in new_board if row == '##########'))
                break
    piece = [''.join(row) for row in zip(*piece[::-1])]

print(max_lines)


