# CCC '21 S2 - Modern Art
# DMOJ: https://dmoj.ca/problem/ccc21s2

def update(diffArr, rStart, cStart, rEnd, cEnd):
    for i in range(rStart, rEnd + 1):
        diffArr[i][cStart] += 1
        diffArr[i][cEnd + 1] -= 1

def printArray(A, D):
    for i in range(N):
        for j in range(M):
            if (j == 0):
                A[i][j] = D[i][j];
            else:
                A[i][j] = D[i][j] + A[i][j - 1];
            print(A[i][j], end = ' ')
        print()


r = int(input())
c = int(input())
k = int(input())

diffArray = [[0 for i in range(c+2)] for j in range(r+2)]

for i in range(k):
    instruction = input().split()
    RorC = instruction[0]
    index = int(instruction[1])

    if RorC == "R":
        update(diffArray, index, 1, index, c)
    else:
        update(diffArray, 1, index, r, index)


print(diffArray)

for i in range(1, r+1):
    for j in range(1, c+1):
        diffArray[i][j] += diffArray[i][j-1]
    for j in range(1, c+1):
        diffArray[i][j] += diffArray[i-1][j]


# Build the diffArray
for i in range(1, r+1):
    for j in range(1, c+1):
        diffArray[i][j] += diffArray[i][j-1]
    for j in range(1, c+1):
        diffArray[i][j] += diffArray[i-1][j]

print(diffArray)


