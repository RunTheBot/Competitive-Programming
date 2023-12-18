# DMOPC '15 Contest 6 P3 - Harvest
#  https://dmoj.ca/problem/dmopc15c6p3
import sys

input = sys.stdin.readline

n, m, minPotatoes = map(int, input().split())
if minPotatoes == 0:
    print(0)
    sys.exit()

diffArray = [0] * (n + 1)
diffArray[0] = 0

for i in range(m):
    start, end = map(int, input().split())
    diffArray[start] -= 1
    if end + 1 < n:
        diffArray[end + 1] += 1

field = [0] * (n + 1)
field[0] = m

#build field from diffArray
for i in range(1, n + 1):
    field[i] = field[i - 1] + diffArray[i]

# for i in range(1, n + 1):
#     # add n to each field
#     field[i] += n

field.pop(0)

# print(field)

# PSA on field
PSA = [0] * (n + 1)
PSA[0] = 0

for i in range(1, n + 1):
    PSA[i] = PSA[i - 1] + field[i - 1]

left, right = 0, 0
minTractor = float('inf')

while right <= n:
    # Check if the current width of the tractor covers at least minPotatoes
    if PSA[right] - PSA[left] >= minPotatoes:
        minTractor = min(minTractor, right - left)
        left += 1
    else:
        right += 1

# If minTractor is still infinity, then there is no solution
if minTractor == float('inf'):
    print(-1)
else:
    print(minTractor)

