# DMOPC '14 Contest 2 P4 - Deforestation
# DMOJ:https://dmoj.ca/problem/dmopc14c2p4

input = __import__('sys').stdin.readline

N = int(input())
treeMasses = [int(input()) for _ in range(N)]
numOfGroups = int(input())

PSA = [0] * (N + 1)
for i in range(N):
    PSA[i + 1] = PSA[i] + treeMasses[i]

for _ in range(numOfGroups):
    a, b = map(int, input().split())
    total_mass = PSA[b + 1] - PSA[a]
    print(total_mass)
