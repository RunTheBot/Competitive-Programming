def permute(str):
    permutations = []
    for i in range(len(str)):
        if str[i] in str[:i]:
            continue
        for permutation in permute(str[:i] + str[i+1:]):
            permutations.append(str[i] + permutation)
    return permutations


match = input()
string = input()

count = 0

for permutation in permute(match):
    if string.find(permutation):
        count += 1

print(count)
