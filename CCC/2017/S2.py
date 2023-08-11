# 2017 Canadian Computing Competition
# Senior Division
# Problem S2: High Tide, Low Tide
# DMOJ: https://dmoj.ca/problem/ccc17s2
import math

length = int(input())
measurements = list(map(int, input().split()))
measurements.sort()

out = []

lowTide = measurements[:math.ceil(length/2)]
highTide = measurements[math.ceil(length/2):]

for i in range(math.ceil(length/2)):
    out.append(lowTide.pop())
    try:
        out.append(highTide.pop(0))
    except IndexError:
        break


print(" ".join(map(str, out)))
