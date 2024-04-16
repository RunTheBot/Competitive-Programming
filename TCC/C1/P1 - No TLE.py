import sys

n = int(input())
votes = input()

yCount = votes.count("Y")
nCount = votes.count("N")

if yCount > nCount:
    print("YES")
    sys.exit()


indexes = []
# Make a list of all the indexes of the N's
for i in range(yCount):
    if votes[i] == "N":
        indexes.append(i)

# prefix_sum = [0] * (n + 1)
# for i in range(1, n + 1):
#     prefix_sum[i] = prefix_sum[i - 1] + (votes[i - 1] == 'Y')
#
# for i in indexes:
#     seen = set()
#
#     for sum in prefix_sum:
#         if sum - i in seen:
#
#         seen.add(sum)
# If there is a N on the first half of the string, then we can always change it to a Y
if votes[n//2:].count("Y") > 0:
    print("YES")
    sys.exit()


print("NO")