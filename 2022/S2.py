pairs = []
enemies = []

violations = 0

for _ in range(int(input())):
    pairs.append(set(input().split(" ")))
    violations += 1

for _ in range(int(input())):
    enemies.append(set(input().split(" ")))

for i in range(int(input())):
    group = set(input().split(" "))
    for i in pairs:
        if i.issubset(group):
            violations -= 1
    for i in enemies:
        if i.issubset(group):
            violations += 1

print(violations)
