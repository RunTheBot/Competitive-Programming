# Segment Tree Problem 1
# DMOJ: https://dmoj.ca/problem/stp2

def build(a, n, segtree):
    for i in range(n):
        segtree[n + i] = a[i]
    for i in range(n - 1, 0, -1):
        segtree[i] = segtree[2 * i] + segtree[2 * i + 1]

def update(index, val, n, segtree):
    index += n
    segtree[index] = val
    while index > 1:
        index //= 2
        segtree[index] = segtree[2 * index] + segtree[2 * index + 1]

def query_tree(left, right, n, segtree):
    left += n
    right += n
    sum = 0
    while left < right:
        if left & 1:
            sum += segtree[left]
            left += 1
        if right & 1:
            right -= 1
            sum += segtree[right]
        left  //= 2
        right //= 2
    return sum

n, q = map(int, input().split())
inputArr = list(map(int, input().split()))

tree = [0] * (2 * n)

build(inputArr, n, tree)

for _ in range(q):
    query = input().split()
    if query[0] == 'S':
        l, r = map(int, query[1:])
        print(query_tree(l - 1, r, n, tree))
    else:
        i, x = map(int, query[1:])
        update(i - 1, x, n, tree)
