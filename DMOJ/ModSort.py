# Modulo Sort
# DMOJ: https://dmoj.ca/problem/modulosort

N = int(input())
K = int(input())

nums = list(map(int, input().split()))

# Using a lambda function with key
# nums = sorted(nums, key=lambda x: x % K)

# Using a tuple with sorted
for i in range(len(nums)):
    nums[i] = (nums[i] % K, nums[i])

nums = sorted(nums)

# print(" ".join(map(str, nums)))
print(" ".join(map(str, [x[1] for x in nums])))