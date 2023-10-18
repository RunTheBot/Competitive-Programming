# CCC '01 S1 - Keeping Score
# Canadian Computing Competition 2001
# DMOJ: https://dmoj.ca/problem/ccc01s1

# Input Processing
oCards = input()

currSuit = ""

cards = {
    "C": [],
    "D": [],
    "H": [],
    "S": []
}

points = {
    "C": 0,
    "D": 0,
    "H": 0,
    "S": 0
}

for card in oCards:
    if card == "C":
        currSuit = "C"
    elif card == "D":
        currSuit = "D"
    elif card == "H":
        currSuit = "H"
    elif card == "S":
        currSuit = "S"
    else:
        cards[currSuit].append(card)

for i in cards:
    if len(cards[i]) == 0:
        points[i] += 3
    elif len(cards[i]) == 1:
        points[i] += 2
    elif len(cards[i]) == 2:
        points[i] += 1
    for card in cards[i]:
        if card == "A":
            points[i] += 4
        elif card == "K":
            points[i] += 3
        elif card == "Q":
            points[i] += 2
        elif card == "J":
            points[i] += 1

# Output
print("Cards Dealt Points")
print("Clubs", " ".join(cards["C"]), points["C"])
print("Diamonds", " ".join(cards["D"]), points["D"])
print("Hearts", " ".join(cards["H"]), points["H"])
print("Spades", " ".join(cards["S"]), points["S"])
print("Total", sum(points.values()))

