# The DMOJ Driveway
# DMOJ: https://dmoj.ca/problem/stack1

T, M = map(int, input().split())

driveway = []

for i in range(T):
    name, action = input().split()
    if action == "in":
        driveway.append(name)
    else:
        if M >= 1 and name == driveway[0]:
            driveway.pop(0)
            M -= 1
        elif name == driveway[-1]:
            driveway.pop(-1)

print("\n".join(driveway))

