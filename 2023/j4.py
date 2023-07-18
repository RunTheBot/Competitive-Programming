n = int(input())
x = [input().split(" "), input().split(" ")]
t = 0

for i in range(0, 2):
    for y in range(0, n):
        if x[i][y] == "1":
            t = t + 3
            if (n-1) != y and x[i][y + 1] == "1":
                t = t - 2
            if y % 2 == 0 and i != 1 and x[i + 1][y] == "1":
                t = t - 2

print(t)
