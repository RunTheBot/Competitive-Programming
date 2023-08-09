#2017 Canadian Computing Competition
#Senior Division
#Problem S3: Nailed It!
#DMOJ: https://dmoj.ca/problem/ccc17s3

blocks = [0 for i in range(2001)]
largest = 0
max_height = 0
num_ways = 0

numBlocks = int(input())

pieces = list(map(int, input().split()))

for blockLength in pieces:
    blocks[blockLength] += 1
    if blockLength > largest:
        largest = blockLength

blocks = blocks[:largest + 1]

for i in range(2, largest * 2 + 1):
    height = 0
    j = max(1, i - largest)
    while j <= i // 2:
        if j != i - j:
            height += min(blocks[j], blocks[i - j])
        else:
            height += blocks[j] // 2
        j += 1
    if height > max_height:
        max_height = height
        num_ways = 1
    elif height == max_height:
        num_ways += 1

print(max_height, num_ways)
