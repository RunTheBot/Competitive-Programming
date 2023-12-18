# Back To School '18: Letter Frequency
# DMOJ: https://dmoj.ca/problem/bts18p1

import numpy as np

fastInput = __import__('sys').stdin.readline

s = fastInput().strip()
#     [[0 for j in range(len(s) + 1)] for i in range(26)]
PSA = [[0 for _ in range(len(s) + 1)] for _ in range(26)]

# ASCII - 97 = index
for i in range(len(s)):
    currChar = s[i]
    index = -1

    # check if it's a lowercase letter
    if currChar.islower():
        index = ord(currChar) - 97
    for j in range(26):
        if j != index:
            PSA[j][i + 1] = PSA[j][i]
        else:
            PSA[j][i + 1] = PSA[j][i] + 1

print(PSA)

Q = int(fastInput())
for _ in range(Q):
    i, j, char = fastInput().split()
    i, j = int(i), int(j)
    char = ord(char) - 97
    print(PSA[char][j] - PSA[char][i - 1])

