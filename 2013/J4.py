from sys import stdin

time = int(stdin.readline())
chores = []

for _ in range(int(stdin.readline())):
    chores.append(int(stdin.readline()))

chores.sort()

done = 0

for chore in chores:
    if time - chore < 0:
        break
    time -= chore
    done += 1

print(done)
