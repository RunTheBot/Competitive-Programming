# UCC 2021 P3: Page Turning
# DMOJ: https://dmoj.ca/problem/ucc21p3

totalLen = int(input())
diffArray = [0]*(totalLen+2)
wanted = input()

for i in range(int(input())):
    [start, end] = list(map(int, input().split()))
    value = 1
    diffArray[start] += value
    diffArray[end+1] -= value

array = []
for i in range(1, totalLen + 1):
    if(i >= 2):
        array.append(array[i - 2] + diffArray[1])
        diffArray.pop(1)
    else:
        array.append(diffArray[1])
        diffArray.pop(1)
del diffArray
wanted = list(map(int, wanted.split()))
out = 0
for i in range(wanted[0], wanted[1]+1):
    out += array[i-1]
print(out)
