# Go Fish
# DMOJ: New problem

a, b = map(int, input().split())

aCount, bCount = 0, 0

cards = input().split()
cardDict = {
    "A": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
    "J": 0,
    "Q": 0,
    "K": 0,
}

for card in cards:
    cardDict[card] += 1

for key in cardDict:
    # print(cardDict[key])
    aCount += cardDict[key] // 2

cards = input().split()
cardDict = {
    "A": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
    "J": 0,
    "Q": 0,
    "K": 0,
}

for card in cards:
    cardDict[card] += 1

for key in cardDict:
    bCount += cardDict[key] // 2

if aCount > bCount:
    print(f'Alice wins with {aCount} pairs')
else:
    print(f'Bob wins with {bCount} pairs')