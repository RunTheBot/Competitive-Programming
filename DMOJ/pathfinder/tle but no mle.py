# You are given an
#  grid with
#  blocked squares and the others open. From an open square, you may move to any other open square that shares an edge with your current square. Please find out whether there is a path from
#  to
# .
#
# Constraints
# For all subtasks:
#
#
#
#
#
# Each given blocked square is unique, and the squares
#  and
#  will not be blocked.
#
# Subtask 1 [15%]
#
# Subtask 2 [85%]
# No additional constraints.
#
# Input Specification
# The first line will contain
#  integers
# ,
# , and
# .
#
# The next
#  lines will each contain
#  integers
#  and
# , representing that square
#  is blocked.
#
# Output Specification
# Output one line containing YES if it is possible to reach
#  from
# , or NO otherwise.


n, m, k = map(int, input().split())

blocks = {}

def in_grid(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    blocks[(x, y)] = True

def BFS(start, end, grid):
    queue = [start]
    visited = set()

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        current = queue.pop(0)
        if current == end:
            return True
        visited.add(current)
        for direction in directions:
            x, y = current
            x += direction[0]
            y += direction[1]
            if in_grid(x, y) and (x, y) not in grid and (x, y) not in visited:
                queue.append((x, y))
    return False

if BFS((0, 0), (n-1, m-1), blocks):
    print("YES")
else:
    print("NO")




