# Guarding a bank during Christmas night can get very boring. That's why Barry decided to go skating around the parking lot for a bit. However the parking lot isn't empty as the other security guards have their cars parked there. So Barry decides to push their cars out of the parking lot. He notices that their cars are parked facing either North, South, East or West. Since the parking lot is frozen, pushing a car will make it slide until it has left the parking lot or hit another car. Cars can only be pushed in the direction which they are facing. Not wanting to crash the cars, Barry enlists your help to find out what order he has to push the cars so as to clear the parking lot.
# The first line contains two integers N and M ( 1 ≤ N , M ≤ 2000 ) representing the number of rows and columns of the parking lot. The next N lines each contain M characters representing the parking lot itself, where . represents an empty spot, while N, S, E and W each represent a car (facing North, South, East or West, respectively).
#
# For at least 70% of the marks for this problem, N ≤ 100 and M ≤ 100 .
#
#Output the order in which the cars have to be pushed so as to clear the parking lot without crashes. Output each car in the form ( r , c ) , where r and c are the car's coordinates on the parking lot (where ( 0 , 0 ) is the top leftmost spot and ( N − 1 , M − 1 ) is the bottom rightmost spot).

#You can assume there will always be at least one valid solution.

#If there are multiple possible solutions, output any valid solution.


# CCO 2015 Problem 4 - Cars on Ice
# DMOJ: https://dmoj.ca/problem/cco15p4

from collections import deque

def bfs(lot, valid, start):
    directions = {'S': (1, 0), 'N': (-1, 0), 'E': (0, 1), 'W': (0, -1)}
    queue = deque([start])

    while queue:
        r, c = queue.popleft()
        print(f'({r},{c})')
        lot[r][c] = '.'
        valid.remove((r, c))

        direction = lot[r][c]
        dr, dc = directions[direction]

        nr, nc = r + dr, c + dc
        while 0 <= nr < len(lot) and 0 <= nc < len(lot[0]) and lot[nr][nc] != '.':
            queue.append((nr, nc))
            nr += dr
            nc += dc

def main():
    n, m = map(int, input().split())

    lot = [list(input()) for _ in range(n)]
    valid = {(i, j) for i in range(n) for j in range(m) if lot[i][j] != '.'}

    while valid:
        start = min(valid)
        bfs(lot, valid, start)

if __name__ == "__main__":
    main()



