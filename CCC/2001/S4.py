from itertools import combinations
import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_circle_from_3_points(p1, p2, p3):
    temp = p2[0] * p2[0] + p2[1] * p2[1]
    bc = (p1[0] * p1[0] + p1[1] * p1[1] - temp) / 2.0
    cd = (temp - p3[0] * p3[0] - p3[1] * p3[1]) / 2.0
    det = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])
    
    if abs(det) < 1e-10:
        return None
    
    center_x = (bc * (p2[1] - p3[1]) - cd * (p1[1] - p2[1])) / det
    center_y = ((p1[0] - p2[0]) * cd - (p2[0] - p3[0]) * bc) / det
    center = (center_x, center_y)
    radius = dist(center, p1)
    return center, radius

def is_valid_circle(center, radius, points):
    return all(dist(center, p) <= radius + 1e-10 for p in points)

def solve(points):
    min_diameter = float('inf')
    
    # Check all pairs of points
    for p1, p2 in combinations(points, 2):
        center = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
        radius = dist(p1, p2)/2
        if is_valid_circle(center, radius, points):
            min_diameter = min(min_diameter, radius * 2)
    
    # Check all triplets of points
    for p1, p2, p3 in combinations(points, 3):
        result = get_circle_from_3_points(p1, p2, p3)
        if result:
            center, radius = result
            if is_valid_circle(center, radius, points):
                min_diameter = min(min_diameter, radius * 2)
    
    return min_diameter

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

print(f"{solve(points):.2f}")
