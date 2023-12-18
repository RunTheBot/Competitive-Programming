import math
from random import random

row, cols = 5, 4
mat = [[math.floor(random()*10) for i in range(cols)] for j in range(row)]
PSA = [[0 for i in range(cols+1)] for j in range(row+1)]

for i in range(row):
    for j in range(cols):
        PSA[i+1][j+1] = PSA[i+1][j] + PSA[i][j+1] - PSA[i][j] + mat[i][j]

print("Matrix:")
print(mat)

print("PSA:")
print(PSA)

x1, y1 = 1, 1
x2, y2 = 2, 3

# Zero-indexed

print(PSA[y2+1][x2+1] - PSA[y2+1][x1] - PSA[y1][x2+1] + PSA[y1][x1])

