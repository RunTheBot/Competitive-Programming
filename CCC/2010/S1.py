
count = int(input())

computers = []

for i in range(count):
    name, ram, cpu, disk = input().split()
    ram = int(ram)
    cpu = int(cpu)
    disk = int(disk)

    performance = 2 * ram + 3 * cpu + disk

    computers.append((performance, name))

sorted_computers = sorted(computers, key=lambda x: (-x[0], x[1]))

try :
    print(sorted_computers[0][1])
    print(sorted_computers[1][1])
except :
    pass





    