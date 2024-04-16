# Educational DP Contest AtCoder A - Frog 1
# DMOJ: https://dmoj.ca/problem/dpa

numStones = int(input())
hights = [0] + list(map(int, input().split()))
dp = [0] * (numStones + 1)

dp[1] = 0
dp[2] = abs(hights[2] - hights[1])

for i in range(3, numStones + 1):
    dp[i] = min(dp[i - 1] + abs(hights[i] - hights[i - 1]), dp[i - 2] + abs(hights[i] - hights[i - 2]))

print(dp[numStones])
