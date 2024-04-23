# Educational DP Contest AtCoder B - Frog 2
# DMOJ: https://dmoj.ca/problem/dpb
import sys

input = sys.stdin.readline

numStones, k = map(int, input().split())
hights = [0] + list(map(int, input().split()))
dp = [0] * (numStones + 1)

dp[1] = 0



if k >= numStones:
    print(abs(hights[numStones] - hights[1]))
    sys.exit(0)

for i in range(1, k+2):
    dp[i] = abs(hights[i] - hights[1])

infin = int(1e18) + 1


for i in range(k+2, numStones + 1):
    best = infin
    for j in range(1, k+1):
        best = min(best, dp[i - j] + abs(hights[i] - hights[i - j]))
    dp[i] = best

print(dp[numStones])
