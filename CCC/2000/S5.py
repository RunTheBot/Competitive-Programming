# DMOJ:  https://dmoj.ca/problem/ccc00s5
n = int(input())

sheep = []
for _ in range(n):
    y = float(input())
    x = float(input())
    sheep.append((y, x))

sheep = sorted(sheep)

def dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

blocked_ranges = []

for i, (y1, x1) in enumerate(sheep):
    can_eat = True
    for start, end in blocked_ranges:
        if start <= x1 <= end:
            can_eat = False
            break
            
    if can_eat:
        x_min = x1
        x_max = x1
        
        for y2, x2 in sheep[i + 1:]:
            d1 = dist((y1, x1), (y2, x2))
            for x in (0, 1000):
                d2 = dist((y2, x2), (y2, x))
                if d2 < d1:
                    if x == 0:
                        x_min = min(x_min, x2)
                    else:
                        x_max = max(x_max, x2)
                        
        blocked_ranges.append((x_min, x_max))
        print(f'The sheep at ({x1:.2f}, {y1:.2f}) might be eaten.')
