# Difference Array template
totalLen = int(input())
diffArray = [0]*(totalLen+2)
out = []

for i in range(int(input())):
    start = int(input())
    end = int(input())
    value = int(input())
    diffArray[start] += value
    diffArray[end+1] -= value

for i in range(1, totalLen + 1):
    if(i >= 2):
        out.append(out[i - 2] + diffArray[i])
    else:
        out.append(diffArray[i])
print(out)
