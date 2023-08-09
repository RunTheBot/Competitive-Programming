# 2000 Canadian Computing Competition
# Senior Division
# Problem S4: Golf
# DMOJ: https://dmoj.ca/problem/ccc00s4

goal = int(input())
clubs = sorted(int(input()) for i in range(int(input())))

counter = 0

for i in clubs:
    while goal - i >= 0:
        goal -= i
        counter += 1
    goal -= i

if goal == 0:
    print("Roberta wins in", counter, "strokes.")
else:
    print("Roberta acknowledges defeat.")
