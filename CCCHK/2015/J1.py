# 2015 CCCHK
# Junior Division
# Problem J1: Rock-paper-scissors
# DMOJ: https://dmoj.ca/problem/ccchk15j1

num = int(input())
Alice  = input().split()
Bob  = input().split()

AliceWins = 0
BobWins = 0

for i in range(num):
    if Alice[i] == "rock" and Bob[i] == "scissors":
        AliceWins += 1
    elif Alice[i] == "paper" and Bob[i] == "rock":
        AliceWins += 1
    elif Alice[i] == "scissors" and Bob[i] == "paper":
        AliceWins += 1
    elif Alice[i] == Bob[i]:
        pass
    else:
        BobWins += 1

print(AliceWins, BobWins)
