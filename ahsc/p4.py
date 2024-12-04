def find_decreases(arr, n):
    return {i for i in range(n) if arr[i] > arr[(i + 1) % n]}

def get_min_shifts(points, n):
    if len(points) == 0: return 0
    if len(points) == 1: return min(next(iter(points)) + 1, n - (next(iter(points)) + 1))
    return -1

n, q = map(int, input().split())
arr = list(map(int, input().split()))
points = find_decreases(arr, n)

for _ in range(q):
    p, v = map(int, input().split())
    p -= 1
    old = arr[p]
    arr[p] = v
    
    prev = (p - 1 + n) % n
    if arr[prev] > arr[p] and prev not in points: points.add(prev)
    elif arr[prev] <= arr[p] and prev in points: points.remove(prev)
    
    if arr[p] > arr[(p + 1) % n] and p not in points: points.add(p)
    elif arr[p] <= arr[(p + 1) % n] and p in points: points.remove(p)
    
    print(get_min_shifts(points, n))
