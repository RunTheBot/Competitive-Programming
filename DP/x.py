import sys
input = sys.stdin.readline


N = int(input().strip())
blocks = [tuple(map(int, input().split())) for _ in range(N)]

blocks.sort(key=lambda b: b[0] + b[1])

dp = {0: 0}
for w, s, v in blocks:
    new_dp = dp.copy()
    for total_w, total_v in dp.items():
        if total_w <= s:
            new_w = total_w + w
            new_v = total_v + v
            new_dp[new_w] = max(new_dp.get(new_w, 0), new_v)
    dp = new_dp
print(max(dp.values()))
