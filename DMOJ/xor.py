# XOR
# DMOJ: https://dmoj.ca/problem/xor

# Given two integers S and F , what is the XOR (exclusive-or) of all numbers between S and F (inclusive)?

def computeXOR(n) :
    if n % 4 == 0 :
        return n
    if n % 4 == 1 :
        return 1
    if n % 4 == 2 :
        return n + 1
    return 0

n = int(input())
for _ in range(n):
    S, F = map(int, input().split())
    print(computeXOR(F) ^ computeXOR(S - 1))


