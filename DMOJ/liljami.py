# Vincent Massey SS - 2014 Senior Contest #1
# DMOJ: https://dmoj.ca/problem/liljami

input = __import__('sys').stdin.readline

N, K = map(int, input().split())
stone_counts = [0] * N

for _ in range(K):
    cup_index = int(input())
    stone_counts[cup_index] += 1

Q = int(input())

PSA = [0]
for i in range(N):
    PSA.append(PSA[-1] + stone_counts[i])

for _ in range(Q):
    a, b = map(int, input().split())
    total_stones = PSA[b + 1] - PSA[a]
    print(total_stones)
