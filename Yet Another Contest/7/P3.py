# Yet Another Contest 7
# Problem P3: No More Math Homework
# DMOJ: https://dmoj.ca/problem/yac7p3

n = int(input())
students = list(range(1, n + 1))
subjects = list(map(int, input().split()))

while True:
    for i in students:
        students = subjects[students]
    
