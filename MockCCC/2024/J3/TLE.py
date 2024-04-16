# Mock CCC '24 Contest 1 J3 - RGB Words
# https://dmoj.ca/problem/mccc6j3

strLen = int(input())
string = input()

# Find the posistions of all the R's, and B's
rPos = set()
bPos = set()

PSA = [0] * (strLen + 1)

for i in range(strLen):
    if string[i] == 'R':
        rPos.add(i)
    elif string[i] == 'B':
        bPos.add(i)
    elif string[i] == 'G':
        PSA[i + 1] = 1
    PSA[i + 1] += PSA[i]

# print(rPos)
# print(bPos)
# print(PSA)

RGBCount = 0

for r in rPos:
    for b in bPos:
        if r < b:
            numG = PSA[b] - PSA[r + 1]
            if numG == 1:
                RGBCount += 1
            elif numG > 1:
                break

print(RGBCount)
