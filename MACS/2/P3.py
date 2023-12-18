# Max's Anger Contest Series 2 P3 - Array Anger
# DMOJ: https://dmoj.ca/problem/macs2p3
import sys
input = sys.stdin.readline

ListSize, NumQueries = map(int, input().split())
List = list(map(int, input().split()))

PSA = [0] * (ListSize + 1)

# Populate PSA
for i in range(ListSize):
    PSA[i + 1] = PSA[i] + List[i]

# Answer the queries
for _ in range(NumQueries):
    OI, start, target = input().split()
    start, target = int(start), int(target)
    PSAStart = PSA[start - 1]

    # print(start, target)

    # Initial check for the val
    if PSA[ListSize] - PSAStart <= target:
        print(ListSize)
        continue

    minVal = start
    maxVal = ListSize

    # Binary search
    while minVal <= maxVal:
        mid = (minVal + maxVal) >> 1
        if target > PSA[mid] - PSAStart:
            minVal = mid + 1
        else:
            maxVal = mid - 1


    print(minVal)
