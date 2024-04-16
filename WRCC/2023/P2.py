for i in range(int(input())):
    # WRCC - Tic Tac Toe

    board = [list(input()) for i in range(3)]
    NextToMove = input().split()[0]

    # for i in range(3):
    #     print(board[i])
    #
    # print(NextToMove)

    if NextToMove == "x":
        Opponent = "o"
    else:
        Opponent = "x"

    shouldContinue = False
    for i in range(3):
        horizontal = board[i][0] + board[i][1] + board[i][2]
        vertical = board[0][i] + board[1][i] + board[2][i]
        # print(horizontal, horizontal.count(NextToMove), horizontal.count(Opponent))
        # print(vertical, vertical.count(NextToMove), vertical.count(Opponent))
        if horizontal.count(NextToMove) == 2 and horizontal.count(Opponent) == 0:
            print(f'{NextToMove} can win')
            shouldContinue = True
            break
        if vertical.count(NextToMove) == 2 and vertical.count(Opponent) == 0:
            print(f'{NextToMove} can win')
            shouldContinue = True
            break

    if shouldContinue:
        continue


    diagonal = board[0][0] + board[1][1] + board[2][2]
    # print(diagonal, diagonal.count(NextToMove), diagonal.count(Opponent))
    if diagonal.count(NextToMove) == 2 and diagonal.count(Opponent) == 0:
        print(f'{NextToMove} can win')
        continue

    diagonal = board[0][2] + board[1][1] + board[2][0]
    # print(diagonal, diagonal.count(NextToMove), diagonal.count(Opponent))
    if diagonal.count(NextToMove) == 2 and diagonal.count(Opponent) == 0:
        print(f'{NextToMove} can win')
        continue
    print("no winning move")


