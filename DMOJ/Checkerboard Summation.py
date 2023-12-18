# Checkerboard Summation (Easy)
# DMOJ: https://dmoj.ca/problem/checkereasy

ySize, xSize = map(int, input().split())
board = [[0 for _ in range(xSize)] for _ in range(ySize)]


while True:
    command = input().split()
    y, x, val = int(command[0]), int(command[1]), int(command[2])
    y, x = y - 1, x - 1

    if command[0] == '0' and command[1] == '0' and command[2] == '0':
        break
    else:
        board[y][x] += val

# print(board)

PSAWhite = [[0 for i in range(xSize+1)] for j in range(ySize+1)]
PSABlack = [[0 for i in range(xSize+1)] for j in range(ySize+1)]



for i in range(ySize):
    isWhite = i % 2 == 0
    for j in range(xSize):
        if isWhite:
            # PSA[i+1][j+1] = PSA[i+1][j] + PSA[i][j+1] - PSA[i][j] + mat[i][j]
            PSAWhite[i+1][j+1] = PSAWhite[i+1][j] + PSAWhite[i][j+1] - PSAWhite[i][j] + board[i][j]
            PSABlack[i+1][j+1] = PSABlack[i+1][j] + PSABlack[i][j+1] - PSABlack[i][j] + 0
        else:
            PSABlack[i+1][j+1] = PSABlack[i+1][j] + PSABlack[i][j+1] - PSABlack[i][j] + board[i][j]
            PSAWhite[i+1][j+1] = PSAWhite[i+1][j] + PSAWhite[i][j+1] - PSAWhite[i][j] + 0
        isWhite = not isWhite

# print(PSAWhite)
# print(PSABlack)
del board, xSize, ySize, i, j, isWhite, val, x, y

while True:
    command = input().split()
    y1, x1, y2, x2 = int(command[0]), int(command[1]), int(command[2]), int(command[3])
    y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1

    if command[0] == '0' and command[1] == '0' and command[2] == '0' and command[3] == '0':
        break
    else:
        # PSA[y2+1][x2+1] - PSA[y2+1][x1] - PSA[y1][x2+1] + PSA[y1][x1]
        whiteSum = PSAWhite[y2+1][x2+1] - PSAWhite[y2+1][x1] - PSAWhite[y1][x2+1] + PSAWhite[y1][x1]
        blackSum = PSABlack[y2+1][x2+1] - PSABlack[y2+1][x1] - PSABlack[y1][x2+1] + PSABlack[y1][x1]

        if y1 % 2 == 0:
            if x1 % 2 == 0:
                print(whiteSum - blackSum)
            else:
                print(blackSum - whiteSum)
        else:
            if x1 % 2 == 0:
                print(blackSum - whiteSum)
            else:
                print(whiteSum - blackSum)
