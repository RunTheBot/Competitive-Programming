# CCC 2010 Senior 4 - Animal Farm
# DMOJ: https://dmoj.ca/problem/ccc10s4

# You are running a farm which has N ( 1 ≤ N ≤ 100 ) animals. You went to the store and bought M = N pre-made pens that will house your animals. Pens satisfy the following conditions:
#
#     pens have between 3 and 8 edges;
#     an edge that is specified by two pens connects the two pens;
#     an edge that is specified only once connects that pen to the outside;
#     there is exactly one animal in each pen and no animals outside the pens, initially.
#
# The animals, however, have a game they like to play called "Escape from the pen." They assign a cost to each edge of the pen, and they determine the minimum cost for all of the animals to meet in the same area by trampling over the edge of various pens. The animals may meet inside a particular pen or outside of all the pens. Also note that once an edge has been trampled, any animal may pass over it without incurring any cost.
#
# You will be given a description of the pens, along with the placement of animals, and you are to figure out what the smallest cost is to move all the animals into the same area.
# Input Specification
#
# The first line of input will be the integer M , the number of pens. On the next M lines, there will be a description of each pen, with one description per line. The description is composed of three components, with each component separated by one space, as follows:
#
#     the first component is an integer e p ( 3 ≤ e p ≤ 8 ), which describes the number of edges for this particular pen p ;
#     the second component is a sequence of e p integers describing the corners of each pen, where each integer is less than or equal to 1 000 ;
#     the third component is a sequence of e p integers describing the cost of each edge, where each integer is less than or equal to 5 000 .
#
# For the corner and edge cost description, the descriptions are given in cyclical order. For example, the following description of a pen
#
# 3   1   2   3   7   4   6
#
# means that there are three corners, and thus, three edges, where the edge ( 1 , 2 ) has cost 7 , the edge ( 2 , 3 ) has cost 4 and the edge ( 3 , 1 ) has cost 6 . Note: at least 20% of the marks for this question have N ≤ 10 and no pen will have more than four edges in these cases.
#
# Note: Due to the official test data being weak, additional test data worth 50 marks has been uploaded. Credit goes to aaronhe07 for noticing the issue and to d for helping sanity check and add data.

def root(pen):
    if parent[pen] != pen:
        return root(parent[pen])
    else:
        return pen

def find(pen1, pen2):
    if root(pen1) != root(pen2):
        return False
    else:
        return True

def union(pen1, pen2):

    rootPen1 = root(pen1)
    rootPen2 = root(pen2)

    if size[rootPen1] > size[rootPen2]:
        parent[rootPen2] = rootPen1
        size[rootPen1] += size[rootPen2]
    else:
        parent[rootPen1] = rootPen2
        size[rootPen2] += size[rootPen1]

m = int(input())
edges = []
for i in range(m):
    e, *data = map(int, input().split())
    edges.append(data)

parent = [i for i in range(1001)]
size = [1] * 1001

graphEdges = []

for i in range(1001):
    for j in range(i, 1001):
        if len(edges[i][j]) == 2:
            graphEdges.append([edges[i][j][0], edges[i][j][1], m])
        elif len(edges[i][j]) == 3:
            graphEdges.append([edges[i][j][0], edges[i][j][1], edges[i][j][2]])

cost1 = 0
edgesUsed = 0

for edge in graphEdges:
    if edge[2] == m:
        continue
    if not find(edge[1], edge[2]):
        cost1 += edge[0]
        edgesUsed += 1
        union(edge[1], edge[2])
    if edgesUsed == m - 1:
        break

parent = [i for i in range(1001)]
size = [1] * 1001

cost2 = 0
edgesUsed2 = 0

for edge in graphEdges:
    if not find(edge[1], edge[2]):
        cost2 += edge[0]
        edgesUsed2 += 1
        union(edge[1], edge[2])
    if edgesUsed2 == m:
        break

print(min(cost1, cost2))
