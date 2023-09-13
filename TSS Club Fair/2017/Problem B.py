# TSS Club Fair 2017
# Problem B
import sys

input = sys.stdin.readline

nums = input().split()
num_houses = int(nums[0])
num_scenarios = int(nums[1])

houses = []
for _ in range(num_houses):
    coords = input().split()
    houses.append(int(coords[0])**2 + int(coords[1])**2)

houses.sort()

# Process each scenario
for _ in range(num_scenarios):
    radius = int(input())

    left = 0
    right = num_houses
    count = 0

    while left < right:
        mid = (left + right) // 2
        if houses[mid] <= radius * radius:
            count = mid + 1
            left = mid + 1
        else:
            right = mid

    print(count)
