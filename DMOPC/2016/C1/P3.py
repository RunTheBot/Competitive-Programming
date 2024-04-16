# DMOPC '16 Contest 1 P3 - Shoe Shopping
# https://dmoj.ca/problem/dmopc16c1p3

numShoes = int(input())
shoePrices = list(map(int, input().split()))
shoePrices = [0] + shoePrices

INF = int(1e9) + 1

if numShoes == 1:
    print(shoePrices[1])
    exit()

if numShoes == 2:
    print(shoePrices[1] + shoePrices[2])
    exit()

dp = [[INF for i in range(4)] for j in range(numShoes + 1)]

deal1_1 = 

