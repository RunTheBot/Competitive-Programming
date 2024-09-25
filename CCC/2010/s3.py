# CCC '10 S3 - Firehose
# DMOJ: https://dmoj.ca/problem/ccc10s3

import sys


def can_cover_all_houses(hose_length, houses, k):
    houses = houses[:]  # Create a copy of the list
    houses.sort()
    houses.extend([h + 1000000 for h in houses])  # Wrap around
    
    for offset in range(h):
        start = offset
        hydrants = 0
        # print((h + offset) - start, len(houses), start, h + offset)
        while start <= h + offset:
            hydrants += 1
            if hydrants > k:
                break
            coverage = houses[start] + 2 * hose_length
            while start < len(houses) and houses[start] <= coverage:
                start += 1
        else:
            return True
    return False
    

# Input
h = int(input())
houses = [int(input()) for _ in range(h)]
k = int(input())

if k >= h:
    print(0)
    sys.exit()
if h == 2:
    # find which way is shorter
    print((min(houses[1] - houses[0], 1000000 - houses[1] + houses[0]) +1)//2)

left, right = 0, 500001  # Max possible hose length is half the circumference
while left < right:
    mid = (left + right) // 2
    if can_cover_all_houses(mid, houses, k):
        right = mid
    else:
        left = mid + 1

# Output
print(left)