import sys

for i in range(int(sys.stdin.readline())):
    n = int(input())
    carts = list(int(input()) for _ in range(n))
    branch = []
    needed = 1

    while carts or branch:
        if carts and carts[-1] == needed:
            carts.pop()
            needed += 1
        elif branch and branch[-1] == needed:
            branch.pop()
            needed += 1
        elif carts:
            branch.append(carts.pop())
        else:
            break

    if carts or branch:
        print("N")
    else:
        print("Y")
