import itertools

permutations = list(map(lambda x: "".join(x), set(itertools.permutations(input()))))

string = input()

count = 0

for permutation in permutations:
    count += string.count(permutation)
    print(permutation, string.count(permutation))
