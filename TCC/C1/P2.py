# The Contest Contest 1 P2 - A Typical CCC Senior Problem
# DMOJ: https://dmoj.ca/problem/tccc1p2

N, K = map(int, input().split())
a = list(map(int, input().split()))
x = list(map(int, input().split()))


for j in range(1, K+1):
    aCopy = a.copy()
    for i in range(N):
        aVal = aCopy[i]

        if aVal == j:
            aCopy[i] = 0
            start_index = max(0, i - j)
            for i in range(start_index, i):
                aCopy[i] = 0
            # print(aCopy)
    print(sum(aCopy))

