# CCC '06 J4 - It's tough being a teen!
# DMOJ: https://dmoj.ca/problem/ccc06j4

nums = []

while True:
    before = int(input())
    after = int(input())


    if before == 0:
        break
    nums.append((before, after))

nums = sorted(nums)

print(" ".join(map(str, [x[0] for x in nums])))