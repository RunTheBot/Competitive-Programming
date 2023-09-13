# Yet Another Contest 7
# Problem P1: Page Turning
# DMOJ: https://dmoj.ca/problem/yac7p1

n = int(input())
pieceLength = list(map(int, input().split()))
totalLength = sum(pieceLength)
oddLengthIndex = []
evenLengthIndex = []
oddLength = []
evenLength = []
startingPage = 1

out = []

inconveniences = 0

for i in range(n):
    if pieceLength[i] % 2 == 0:
        evenLengthIndex.append(i)
        evenLength.append(pieceLength[i])
    else:
        oddLength.append(pieceLength[i])
        oddLengthIndex.append(i)


for i in range(max(len(oddLengthIndex), len(evenLengthIndex))):
    try:
        inconveniences += (oddLength[i]) // 2
        startingPage += (oddLength[i])
        out.append(str(oddLengthIndex[i] + 1))
    except:
        pass
    try:
        inconveniences += (evenLength[i] - 1 if startingPage % 2 == 0 else 0) // 2
        startingPage += (evenLength[i])
        out.append(str(evenLengthIndex[i] + 1))
    except:
        pass

print(inconveniences)
print(" ".join(out))

# 5
# 3 5 4 2 2 2
# bad
