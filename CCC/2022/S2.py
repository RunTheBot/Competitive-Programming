from collections import defaultdict
pairs = defaultdict(set)
enemies = defaultdict(set)
violations = 0

for i in range(int(input())):
    pair = input().split()
    pairs[pair[0]].add(pair[1])
    violations += 1

for i in range(int(input())):
    enemy = input().split()
    enemies[enemy[0]].add(enemy[1])

for _ in range(int(input())):
    group = input().split()
    for person in group:
        for enemy in enemies[person]:
            if enemy in group:
                violations += 1
        for pair in pairs[person]:
            if pair in group:
                violations -= 1

print(violations)
