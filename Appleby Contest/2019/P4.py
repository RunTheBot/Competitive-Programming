N = int(input())

points = set()

for i in range(N):
    x, y = map(int, input().split())
    points.add((x, y))


out = 0

for i, point1 in enumerate(points):
    x1, y1 = point1
    for j, point2 in enumerate(points):
        x2, y2 = point2
        if x1 != x2 and y1 != y2:
            if (x1, y2) in points and (x2, y1) in points:
                out = max(out, abs(y2 - y1) * abs(x2 - x1))

print(out)
