length = input()
day1 = input()
day2 = input()

out = 0

for i in range(int(length)):
    if day1[i] == day2[i] == "C":
        out += 1
print(out)
