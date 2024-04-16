import sys

n = int(input())
votes = input()

yCount = votes.count("Y")
nCount = votes.count("N")

if yCount > nCount:
    print("YES")
    sys.exit()

if nCount-1 < yCount+1:
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (votes[i - 1] == 'Y')

    for i in range(n):
        for j in range(i, n):
            interval_size = j - i + 1
            interval_yes = prefix_sum[j + 1] - prefix_sum[i]

            if interval_yes > 0:
                index = interval_yes - 1
                if votes[index] == "N":
                    print("YES")
                    sys.exit()

print("NO")
sys.exit()