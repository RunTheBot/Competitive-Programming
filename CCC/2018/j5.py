# CCC '18 J5 - Choose your own path
# Canadian Computing Competition 2018
# DMOJ: https://dmoj.ca/problem/ccc18j5

def BFS(book, length):
    queue = [(1, 1)]
    visited = [False for _ in range(length)]
    ended = False
    endMoves = -1

    visited[0] = True

    while len(queue) > 0:
        currentPage, moves = queue.pop(0)
        if book[currentPage] == [0]:
            if not ended:
                ended = True
                endMoves = moves
            if moves < endMoves:
                endMoves = moves
        for nextPage in book[currentPage]:
            if not visited[nextPage-1]:
                visited[nextPage-1] = True
                queue.append((nextPage, moves+1))
    return (visited, endMoves)

# Input Processioning

length = int(input())

book = [[]]

for i in range(length):
    option = list(map(int, input().split()))
    book.append(option)

# for option in book:
#     print(" ".join(list(map(str, option))))
#
# print(length)

# Output
visited, moves = BFS(book, length)

if False in set(visited):
    print("N")
else:
    print("Y")
print(moves)


