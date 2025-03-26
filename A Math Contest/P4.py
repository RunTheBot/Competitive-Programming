import math

N = int(input())

def find_c(theta):
    if theta == 0:
        return 0.0
    if theta > 0:
        low = 0.0
        high = 1.0
    else:
        low = -1.0
        high = 0.0
    for _ in range(100):
        mid = (low + high) / 2
        f_mid = math.asin(mid) + mid * math.sqrt(1 - mid * mid)
        if f_mid < theta:
            low = mid
        else:
            high = mid
    return mid

cs = []
for i in range(1, N):
    theta = math.pi / 2 - (i * math.pi) / N
    c = find_c(theta)
    cs.append(c)

cs.sort()

for c in cs:
    print("{0:.9f}".format(c))