# Don Mills Programming Gala 2015
# Senior Division
# Problem 3: The Great Escape
# DMOJ: https://dmoj.ca/problem/dmpg15s3

numFlowers = int(input())
flowers = list(map(int, input().split()))
numBad = int(input())
bad = [list(map(int, input().split())) for i in range(numBad)]
out = 0

for i in bad:
    pos = i[0]
    value = i[1]
    pairPos = pos - 1
    if flowers[pos - 1] < value or flowers[pos] < value:
        flowers[pairPos if flowers[pairPos] < flowers[pos] else pos] = 0
    else:
        flowers.append(-value)

print(sum(flowers))
