import math

nums = list(map(int, input().split()))

houses = []

for _ in range(nums[0]):
    coords = list(map(int, input().split()))
    houses.append(math.sqrt(coords[0]**2 + coords[1]**2))
for _ in range(nums[1]):
    radius = int(input())
    count = 0
    for house in houses:
        if house <= radius:
            count += 1
    print(count)
