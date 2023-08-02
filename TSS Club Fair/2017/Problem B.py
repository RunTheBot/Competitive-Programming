import math

nums = list(map(int, input().split()))

houses = []

for _ in range(nums[0]):
    coords = list(map(int, input().split()))
    houses.append(math.sqrt(coords[0]**2 + coords[1]**2))

houses.sort()

# print(houses)
for _ in range(nums[1]):
    radius = int(input())
    current = 0
    count = 0
    bombedHouses = houses.copy()
    # find when houses stops to get bombed
    for i in range(len(houses)):
        if houses[i] > radius:
            current = i
            break

    print(current)
