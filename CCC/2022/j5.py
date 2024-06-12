# CCC '22 J5 - Square Pool
# https://dmoj.ca/problem/ccc22j5

# Ron wants to build a square pool in his square -by- yard, but his yard contains
#
# trees. Your job is to determine the side length of the largest square pool he can build.
# Input Specification
#
# The first line of input will be an integer
# with . The second line will be the positive integer where . The remaining input will be lines, each representing the location of a single tree. The location is given by two positive integers, and then , separated by a single space. Each tree is located at row and column where rows are numbered from top to bottom from to and columns are numbered from left to right from to
#
# . No two trees are at the same location.
#
# The following table shows how the available 15 marks are distributed.

# n = int(input())
# trees = [[int(x) for x in input().split()] for _ in range(int(input()))]
# trees.append([0, 0])
# tX = [x[0] for x in trees]
# tY = [x[1] for x in trees]
# ans = 0
# for x in tX:
#     for y in tY:
#         s = min(n - y, n - x)
#         for a, b in trees:
#             if x < a and y < b:
#                 s = min(s, max(a - x, b - y) - 1)
#         ans = max(ans, s)
# print(ans)

n = int(input())
tree_x = []
tree_y = []

for _ in range(int(input())):
    x, y = map(int, input().split())
    tree_x.append(x)
    tree_y.append(y)

tree_x.append(0)
tree_y.append(0)

ans = 0

for x in tree_x:
    for y in tree_y:
        minDist = min(n - x, n - y)
        for a, b in zip(tree_x, tree_y):
            if x < a and y < b:
                minDist = min(minDist, max(a - x, b - y) - 1)
        ans = max(ans, minDist)

print(ans)
