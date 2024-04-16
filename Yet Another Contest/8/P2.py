# Yet Another Contest 8 P2 - No More Modern Art
# DMOJ: https://dmoj.ca/problem/yac8p2
import sys

n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

num_dict = {}
for num in a:
    if num_dict.get(num ^ x):
        print("YES")
        sys.exit()
    num_dict[num] = True

print("NO")