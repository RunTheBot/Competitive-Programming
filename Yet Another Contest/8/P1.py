def longest_increasing_subsequence(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


n = int(input())
nums = list(map(int, input().split()))
print(n - longest_increasing_subsequence(nums))
