cost = {
    "S": 1,
    "M": 5,
    "L": 10
}


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def BFS(graph, start, visited, wall):
    queue = [start]
    count = 0
    total = 0
    while len(queue) > 0:
        current = queue.pop(0)
        # print(cost[graph[current[0]][current[1]]])
        # print(graph[current[0]][current[1]])
        count += cost[graph[current[0]][current[1]]]
        # total += 1
        for direction in directions:
            try:
                next = (current[0] + direction[0], current[1] + direction[1])
                # print(graph[next[0]][next[1]])
                # print(visited[next[0]][next[1]])
                if not visited[next[0]][next[1]] and graph[next[0]][next[1]] != wall:
                    visited[next[0]][next[1]] = True
                    queue.append(next)
            except:
                pass

    # print(total)
    return count

"""
6
6
**LMLS
S*LMMS
S*SMSM
******
LLM*MS
SSL*SS
5
1
"""

R = int(input())
C = int(input())

graph = []
graph.append("*"*(R+2))

for _ in range(R):
    graph.append("*"+input()+"*")

graph.append("*"*(R+2))

# print(graph)

startRow = int(input())+1
startCol = int(input())+1

visted = [[False for i in range(C+2)] for j in range(R+2)]

# print(startCol, startRow)

visted[startRow][startCol] = True

# print(graph[startRow][startCol])

print(BFS(graph,(startRow, startCol), visted, "*"))

