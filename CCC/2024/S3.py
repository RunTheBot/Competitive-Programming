import sys

arrLen = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

# print(arrA, arrB)

if arrA == arrB:
    print("YES")
    print("0")
    sys.exit()


prevDiffIndex = None
diffStart = None
diffEnd = None
targetVal = None

for i in range(arrLen):
    # print(arrLen, len(arrA), len(arrB))
    if arrA[i] != arrB[i]:
        if prevDiffIndex is None:
            prevDiffIndex = i
            diffStart = i
            diffEnd = i
            targetVal = arrB[i]
        else:
            diffEnd = i

            if prevDiffIndex+1 != i:
                print("NO")
                sys.exit()
            if arrA[i] != targetVal:
                print("NO")
                sys.exit()

            prevDiffIndex = i

possiblities = [(diffStart, diffEnd), (diffStart-1, diffEnd), (diffStart, diffEnd+1)]

for start, end in possiblities:
    if arrA[start] == targetVal:
        print('YES')
        print(1)
        print(f'R {start} {end}')
        break

    elif arrA[end] == targetVal:
        print('YES')
        print(1)
        print(f'L {start} {end}')
        break




