# Summer Institute '17 Contest 1 P8 - Mo' Money
# DMOJ: https://dmoj.ca/problem/si17c1p8

def helper(index, remaining):
    if remaining == 0:
        return 1
    if remaining < 0 or index == len(coins):
        return 0

    # Try including the current coin and excluding it
    include_current = helper(index, remaining - coins[index])
    exclude_current = helper(index + 1, remaining)

    return include_current + exclude_current

# Read input
n, target = map(int, input().split())
coins = list(map(int, input().split()))

# Output the result
print(helper(0, target))
