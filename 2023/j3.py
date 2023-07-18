n = int(input())
x = [0,0,0,0,0]
d = [0]

for i in range(0, n):
    array = input()
    for i in range(0, 5):
        if array[i] == "Y":
            x[i] = x[i] + 1

max = 0

for i in range(0,5):
    if x[i] > max:
        d.clear()
        max = x[i]
        d.append(i+1)
    elif max == x[i]:
        d.append(i+1)

print(str(d).replace("[","").replace("]","").replace(" ",""))
