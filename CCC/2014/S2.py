# 2014 Canadian Computing Competition
# Senior Division
# Problem S2: Assigning Partners
# DMOJ: https://dmoj.ca/problem/ccc14s2
from collections import defaultdict
from sys import exit

numStudents = int(input())
group1 = input().split()
group2 = input().split()

pairs = defaultdict(str)

for i in range(numStudents):
    if group1[i] == group2[i]:
        print("bad")
        exit()
    else:
        if pairs[group1[i]] != "" and pairs[group1[i]] != group2[i]:
            print("bad")
            exit()
        pairs[group1[i]] = group2[i]
        pairs[group2[i]] = group1[i]

print("good")
