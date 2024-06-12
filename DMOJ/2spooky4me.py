# Kenny wants to go trick-or-treating too! But the street has many spooky decorations put up on it. Kenny doesn't like to be scared, so he avoids spooky areas.
#
# There are L houses arranged in a line on the street, numbered from 1 to L . Each house will give exactly 1 unit of candy to Kenny. There are N spooky decorations on this street. The i -th decoration covers the street from house number a i to b i , inclusive, raising the spookiness of those houses by s i spookiness units.
#
# Kenny will be too scared to knock on any doors if the spookiness of a house is greater than or equal to S . The spookiness of a house is the sum of the spookinesses of all the decorations passing through it.
#
# Determine the amount of candy Kenny can receive from all the houses on the street.

# 2spooky4me | PEG Test - Halloween 2014
# DMOJ: https://dmoj.ca/problem/2spooky4me
num_deco, num_houses, spook_limit = map(int, input().split())

PSA = [(num_houses + 1, 0)]

for _ in range(num_deco):
    start, end, spookiness = map(int, input().split())
    PSA.append((start, spookiness))
    PSA.append((end + 1, -spookiness))

PSA.sort()
current = 0
for i in range(len(PSA)-1):
    current += PSA[i][1]
    if current >= spook_limit:
        num_houses -= PSA[i+1][0] - PSA[i][0]

print(num_houses)

