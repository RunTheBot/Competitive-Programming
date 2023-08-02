#2021 Canadian Computing Competition
#Junior Division
#Problem J4: Arranging Books
#DMOJ: https://dmoj.ca/problem/ccc21j4

shelf = input()
Ls =  shelf.count("L")
Ms = shelf.count("M")
Ss = shelf.count("S")

lSection = shelf[:Ls]
mSection = shelf[Ls:Ls+Ms]
sSection = shelf[Ls+Ms:]

print(max(lSection.count("S"), sSection.count("L")) + (Ms-mSection.count("M")))
