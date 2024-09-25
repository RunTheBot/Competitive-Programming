# Amplitude Hackathon Summer '24 Problem 1 - Is Jeffrey in the Office?
# DMOJ: https://dmoj.ca/problem/ampl2024sp1

# You know what day today is. Is Jeffrey in the office? It is well-known he is in the office if and only if it is a weekday - that is, not Saturday nor Sunday.

s = input()

if s == "Saturday" or s == "Sunday":
    print("NO")
else:
    print("YES")
