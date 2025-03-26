n, capacity = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

max_val = sum(v for _, v in items)  
INF = 10**18  

dp = [INF] * (max_val + 1)
dp[0] = 0

for item_weight, item_value in items:
    for val in range(max_val, item_value - 1, -1):  
        dp[val] = min(dp[val], dp[val - item_value] + item_weight)

print(max(v for v in range(max_val + 1) if dp[v] <= capacity))