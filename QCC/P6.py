# Quarantine Computing Competition: Problem 6
# QCC P6 - Freedom!
# DMOJ: https://dmoj.ca/problem/qcc6

input = __import__("sys").stdin.readline

# Read input
N = int(input())
heights = list(map(int, input().split()))

psa = [0] * (N + 1)
for i in range(2, N + 1):
    psa[i] = psa[i - 1] + abs(heights[i - 1] - heights[i - 2]) * (i - 1)

ssa = [0] * (N + 1)
for i in range(N - 1, 0, -1):
    ssa[i] = ssa[i + 1] + abs(heights[i] - heights[i - 1]) * (N - i)

# # Print debug information
# print("Prefix Sum Array (psa):", psa)
# print("Suffix Sum Array (ssa):", ssa)

Q = int(input())

# Answer each query
for _ in range(Q):
    hi = int(input())
    total_cost = psa[hi] + ssa[hi]

    # Print debug information for each query
    # print(f"Query for hi={hi}: psa[{hi}] = {psa[hi]}, ssa[{hi}] = {ssa[hi]}, total_cost = {total_cost}")
    print(total_cost)
