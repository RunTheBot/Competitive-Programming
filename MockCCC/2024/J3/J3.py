# Mock CCC '24 Contest 1 J3 - RGB Words
# https://dmoj.ca/problem/mccc6j3

strLen = int(input())
string = input()

gPos = []

PSAR = [0] * (strLen + 1)
PSAB = [0] * (strLen + 1)

for i in range(strLen):

    if string[i] == 'R':
        PSAR[i + 1] = 1
    elif string[i] == 'B':
        PSAB[i + 1] = 1
    elif string[i] == 'G':
        gPos.append(i)
    PSAR[i + 1] += PSAR[i]
    PSAB[i + 1] += PSAB[i]

RGBCount = 0

for gIndexIndex in range(len(gPos)):
    currG = gPos[gIndexIndex]
    prevG = gPos[gIndexIndex - 1] if gIndexIndex > 0 else 0
    nextG = gPos[gIndexIndex + 1] if gIndexIndex < len(gPos) - 1 else strLen
    # find the number of R's from prevG to g
    RCount = PSAR[currG] - PSAR[prevG]
    # find the number of B's from g to the next G
    BCount = PSAB[nextG] - PSAB[currG]

    RGBCount += RCount * BCount


print(RGBCount)
