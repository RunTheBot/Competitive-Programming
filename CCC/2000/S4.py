# 2000 Canadian Computing Competition
# Senior Division
# Problem S4: Golf
# DMOJ: https://dmoj.ca/problem/ccc00s4

distance = int(input())
num_clubs = int(input())
clubs = [int(input()) for _ in range(num_clubs)]


INF = float('inf')
dp = [INF] * (distance + 1)
dp[0] = 0

for i in range(1, distance + 1):
    for club in clubs:
        if i - club >= 0:
            dp[i] = min(dp[i], dp[i - club] + 1)

if dp[distance] != INF:
    print(f"Roberta wins in {dp[distance]} strokes.")
else:
    print("Roberta acknowledges defeat.")
