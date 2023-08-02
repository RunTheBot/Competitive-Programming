# 2015 Canadian Computing Competition
# Senior Division
# Problem S1: Zero That Out
# DMOJ: https://dmoj.ca/problem/ccc15s1

output = []

for i in range(int(input())):
    num = int(input())
    if num == 0:
        output.pop()
    else:
        output.append(num)
print(sum(output))

