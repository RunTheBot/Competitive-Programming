def permutate(l):
    for i, x in enumerate(l):
        for y in l[i + 1:]:
            yield x

permutations = list(map(lambda x: "".join(x), set(itertools.permutations(input()))))

string = input()

count = 0

for permutation in permutations:
    if string.count(permutation) > 0:
        count += 1

print(count)
