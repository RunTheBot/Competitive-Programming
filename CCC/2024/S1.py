n = int(input())
hats = [input() for i in range(n)]

# print(hats)

out = 0

for i in range(n//2):
    if hats[i] == hats[i + n//2]:
        out += 2

print(out)