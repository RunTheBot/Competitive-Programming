# Educational DP Contest AtCoder H - Grid 1
# DMOJ: https://dmoj.ca/problem/dph

height, width = list(map(int, input().split()))
grid = [list(input()) for i in range(height)]

dp = [[0 for i in range(width)] for j in range(height)]
dp[0][0] = 1

for i in range(height):
    for j in range(width):
        if grid[i][j] == "#":
            dp[i][j] = 0
            continue
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]
        dp[i][j] %= 1000000007 # Modulo 10^9 + 7

print((dp[height - 1][width - 1]))