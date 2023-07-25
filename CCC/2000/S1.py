points = int(input())
machines = [int(input()), int(input()), int(input())]
counter = 0

whenPay = [35, 100, 10]
pointsOut = [30, 60, 9]

while points > 0:
    machineNumber = counter % 3

    machines[machineNumber] += 1

    if machines[machineNumber] == whenPay[machineNumber]:
        points += pointsOut[machineNumber]
        machines[machineNumber] = 0

    points -= 1
    counter += 1

print("Martha plays " + str(counter) + " times before going broke.")
