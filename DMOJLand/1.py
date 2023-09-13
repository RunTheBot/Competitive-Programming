# DMOJ Land Series
# Fake Judges
# DMOJ: https://dmoj.ca/problem/dland1

n, q = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
for i in range(q):
    l, r = map(int, input().split())
    t = sum(a[l-1:r])
    print((s-t) * t)