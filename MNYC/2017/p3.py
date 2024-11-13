# MNYC '17: Hurontario
# DMOJ: https://dmoj.ca/problem/mnyc17p3

input = __import__('sys').stdin.readline

A, B = input().split()

MOD = 10**9 + 7  
BASE = 31        
len_A = len(A)
len_B = len(B)

hash_A = 0
hash_B = 0
power = 1

max_overlap = 0

for i in range(1, min(len_A, len_B) + 1):
    hash_A = (hash_A + ord(A[len_A - i]) * power) % MOD
    hash_B = (hash_B * BASE + ord(B[i - 1])) % MOD
    
    if hash_A == hash_B:
        max_overlap = i
    
    power = (power * BASE) % MOD  


print(A + B[max_overlap:])

