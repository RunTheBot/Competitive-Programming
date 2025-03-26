""" In the example above, the bricks are represented by capital O's and the floor is a row of equal signs. The original board 
(
1
)
 is rotated 
180
 degrees 
(
2
)
, then the floor of the board is moved to the bottom 
(
3
)
, then the pieces all settle to the new floor 
(
4
)
 making a single complete row which gets removed 
(
5
)
.

The input contains five different Upsetris boards, each with from 
5
 to 
20
 rows (not including the "floor") and from 
5
 to 
20
 columns (not including the walls). You must simulate the "upset" operation and show the final result for each board. You must show the complete board in your output, including the "floor" row.

Note that all the boards in the sample input are the same size and have the same number of rows as columns, but this might not be true of the data sets you will be judged on. The side characters for the board | are ASCII code 
124
.

Sample Input
Copy
|          |
|          |
|O         |
|O OO  O O |
|    O O   |
| O   O OO |
|  O     OO|
|O O       |
|   O  O O |
|O      O  |
|==========|
|          |
|          |
|          |
|    O     |
|   O  OO O|
|   O     O|
|    O  O  |
|       OO |
|O         |
|   O     O|
|==========|
|          |
|          |
|          |
|          |
| O   OOO O|
|O O  OOOO |
|  O O OO O|
| OO OOOOO |
|     OOOOO|
|OO OOOOO O|
|==========|
|          |
|          |
|          |
|          |
|          |
|          |
|          |
|          |
| O     O  |
|     O   O|
|==========|
|          |
|          |
|          |
|          |
|OO OO OOOO|
| O OOOOOOO|
|O OOOO OOO|
| OOOOOOOO |
|OOOO O O  |
|O  OOO OOO|
|==========|
Sample Output
Copy
|          |
|          |
|          |
|          |
|          |
|          |
|          |
| O       O|
| O O   O O|
| OOO  OO O|
|==========|
|          |
|          |
|          |
|          |
|          |
|          |
|          |
|O O   O   |
|O O  OO   |
|OOOO OO  O|
|==========|
|          |
|          |
|          |
|          |
|          |
|  OO      |
|  OOO     |
|O OOO     |
|OOOOOO OO |
|OOOOOO OOO|
|==========|
|          |
|          |
|          |
|          |
|          |
|          |
|          |
|          |
|          |
|O O O   O |
|==========|
|          |
|          |
|          |
|          |
|          |
|          |
|          |
|  O   O   |
| OO OOO   |
|OOO OOO OO|
|==========| """

for _ in range(5):
    # input
    board = []
    
    stripped_len = 0
    row = input()[1:-1]
    width = len(row)
    if row != " " * width:
        board.append(row)
    while True:
        row = input()[1:-1][::-1]
        if row == "=" * width:
            break
        if row != " " * width:
            board.append(row)
        else:
            stripped_len += 1
    
    length = len(board)
    
    # print the board
    # print()
    # for i in range(length):
    #     print("|" + board[i] + "|")
    
    # rotate the board 90 degrees
    roatated_board = list(zip(*board[::-1]))
    
    
    # print()
    # # print the rotated board
    # print("_" * (width + 2))
    # for i in range(width):
    #     print("".join(roatated_board[i]))
    
    # print("_" * (width + 2))
    
    min_count = 100
    for i in range(width):
        count = roatated_board[i].count("O")
        if count < min_count:
            min_count = count
        roatated_board[i] = " " * (length - count)+ "O" * count
    
    
    # print()
    # # print the rotated board
    # print("_" * (width + 2))
    # for i in range(width):
    #     print("".join(roatated_board[i]))
    
    # print("_" * (width + 2))
    
    board = list(zip(*roatated_board))
    
    # print the rotated board
    # print()
    # for i in range(length):
    #     print("|" + "".join(board[i]) + "|")
    
    # print(min_count)
    if min_count > 0:
        board = board[:-min_count]
    
    # print()
    # for i in range(length):
    #     print("|" + "".join(board[i]) + "|")
    
    # print("result")
    
    print("|" + " " * width + "|")
    for i in range(min_count):
        print("|" + " " * width + "|")
    
    for i in range(stripped_len):
        print("|" + " " * width + "|")
    
    for row in board:
        print("|" + "".join(row) + "|")
        # print(row)
    print("|"+"=" * width+"|")
    