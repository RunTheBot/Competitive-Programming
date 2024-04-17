# CCC '20 S2 - Escape Room
# URL: https://dmoj.ca/problem/ccc20s2

"""
Canadian Computing Competition: 2020 Stage 1, Junior #5, Senior #2

You have to determine if it is possible to escape from a room. The room is an M -by- N grid with each position (cell) containing a positive integer. The rows are numbered 1 , 2 , … , M and the columns are numbered 1 , 2 , … , N . We use ( r , c ) to refer to the cell in row r and column c .

You start in the top-left corner at ( 1 , 1 ) and exit from the bottom-right corner at ( M , N ) . If you are in a cell containing the value x , then you can jump to any cell ( a , b ) satisfying a × b = x . For example, if you are in a cell containing a 6 , you can jump to cell ( 2 , 3 ) .

Note that from a cell containing a 6 , there are up to four cells you can jump to: ( 2 , 3 ) , ( 3 , 2 ) , ( 1 , 6 ) , or ( 6 , 1 ) . If the room is a 5 -by- 6 grid, there isn't a row 6 so only the first three jumps would be possible.
Input Specification

The first line of the input will be an integer M ( 1 ≤ M ≤ 1 000 ) . The second line of the input will be an integer N ( 1 ≤ N ≤ 1 000 ) . The remaining input gives the positive integers in the cells of the room with M rows and N columns. It consists of M lines where each line contains N positive integers, each less than or equal to 1 000 000 , separated by single spaces.

For 1 of the 15 available marks, M = 2 and N = 2 .

For an additional 2 of the 15 available marks, M = 1 .

For an additional 4 of the 15 available marks, all of the integers in the cells will be unique.

For an additional 4 of the 15 available marks, M ≤ 200 and N ≤ 200 .
"""

from collections import deque

def findFactors(num):

    factors = []

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if num // i == i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(num // i)

    return factors

def isInside(mazeSize, pose):
    return 0 <= pose[0] < mazeSize[0] and 0 <= pose[1] < mazeSize[1]


def BFS(start, end, maze):
    mazeSize = (len(maze), len(maze[0]))
    queue = [start]
    visited = [[False for i in range(mazeSize[1]+1)] for j in range(mazeSize[0]+1)]

    while len(queue) > 0:
        current = queue.pop()

        currentVal = maze[current[0]][current[1]]

        for factor in findFactors(currentVal):
            nextPossiblePos = (factor-1, (currentVal // factor)-1)
            if isInside(mazeSize, nextPossiblePos):
                if nextPossiblePos == end:
                    return True
                if not visited[nextPossiblePos[0]][nextPossiblePos[1]]:
                    visited[nextPossiblePos[0]][nextPossiblePos[1]] = True
                    queue.append(nextPossiblePos)

    return False


M = int(input())
N = int(input())
maze = []

for i in range(M):
    maze.append(list(map(int, input().split())))

start = (0, 0)
end = (M-1, N-1)

if BFS(start, end, maze):
    print("yes")
else:
    print("no")

