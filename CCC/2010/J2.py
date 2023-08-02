# 2010 Canadian Computing Competition
# Junior Division
# Problem J2: Up and Down
# DMOJ: https://dmoj.ca/problem/ccc10j2

NikkyPlus = int(input())
NikkyMinus = int(input())
NikkyPerRound = NikkyMinus + NikkyPlus
NikkyTotal = 0
ByronPlus = int(input())
ByronMinus = int(input())
ByronPerRound = ByronMinus + ByronPlus
ByronTotal = 0

total = int(input())

while NikkyTotal + NikkyPerRound <= total:
    NikkyTotal += NikkyPerRound
    Nikky += 1



