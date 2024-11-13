# CCC '03 S4: Substrings
# DMOJ: https://dmoj.ca/problem/ccc03s4

t = int(input())

for _ in range(t):
    s = input()
    suffix_array = sorted(range(len(s)), key=lambda i: s[i:])
    n = len(s)
    rank = [0] * n
    lcp = [0] * n
    h = 0
    
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    
    total_substrings = n * (n + 1) // 2
    distinct_substrings = total_substrings - sum(lcp)
    
    print(distinct_substrings + 1)