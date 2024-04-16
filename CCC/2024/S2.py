import sys

n, length = map(int, input().split())

# print(n)

for i in range(n):
    string = input()
    # print(string)
    if length > 53:
        print("F")
        continue

    charSet = set(string)
    heavyLetters = set()

    for char in charSet:
        if string.count(char) > 1:
            heavyLetters.add(char)

    firstHeavyLetter = None

    for charIndex in range(2):
        if string[charIndex] in heavyLetters:
            firstHeavyLetter = charIndex
            break

    if firstHeavyLetter is None:
        print("F")
        continue

    for i in range(firstHeavyLetter, length, 2):
        try:
            if string[i] not in heavyLetters:
                print("F")
                break
        except:
            continue

        try:
            if string[i + 1] in heavyLetters:
                # print(string[i] + string[i + 1])
                print("F")
                break
        except:
            continue
    else:
        print("T")






