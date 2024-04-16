# Educational DP Contest AtCoder D - Knapsack 1
# DMOJ: https://dmoj.ca/problem/dpd

numItems, capacity = map(int, input().split())
knapsack_values = [0] * (capacity + 1)

for _ in range(numItems):
    itemWeight, itemValue = map(int, input().split())
    for currentWeight in range(capacity, itemWeight - 1, -1):
        knapsack_values[currentWeight] = max(knapsack_values[currentWeight - itemWeight] + itemValue, knapsack_values[currentWeight])

print(max(knapsack_values))
