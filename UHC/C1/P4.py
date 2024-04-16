n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort()
xMedian = points[n // 2][0]

points.sort(key=lambda p: p[1])
yMedian = points[n // 2][1]

totalDistance = 0
for x, y in points:
    totalDistance += abs(x - xMedian) + abs(y - yMedian)

neighborDistances = []
for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
        nx = xMedian + dx
        ny = yMedian + dy
        distance = 0
        for x, y in points:
            distance += abs(x - nx) + abs(y - ny)
        neighborDistances.append((distance, (nx, ny)))

minNeighborDistance, minNeighborPoint = min(neighborDistances)

# print(xMedian, yMedian, min_neighbor_point)

print(totalDistance + minNeighborDistance)