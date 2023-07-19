n = int(input())
deck = input().split(" ")

count = 0

for i in range(n):
    if deck[i] == deck[i+n]:
        count += 1

print(count)
