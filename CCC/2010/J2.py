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

NikkyPos = 0
ByronPos = 0

total = int(input())

while NikkyTotal + NikkyPerRound <= total:
    NikkyTotal += NikkyPerRound
    NikkyPos += NikkyPlus
    NikkyPos -= NikkyMinus

if NikkyTotal < total:
    if (total - NikkyTotal) < NikkyPlus:
        NikkyPos += total - NikkyTotal
    else:
        NikkyPos += NikkyPlus
        NikkyTotal += NikkyPlus
        NikkyPos -= total - NikkyTotal

while ByronTotal + ByronPerRound <= total:
    ByronTotal += ByronPerRound
    ByronPos += ByronPlus
    ByronPos -= ByronMinus

if ByronTotal < total:
    if (total - ByronTotal) < ByronPlus:
        ByronPos += total - ByronTotal
    else:
        ByronPos += ByronPlus
        ByronTotal += ByronPlus
        ByronPos -= total - ByronTotal

print("Nikky" if NikkyPos > ByronPos else "Byron" if ByronPos > NikkyPos else "Tied")



