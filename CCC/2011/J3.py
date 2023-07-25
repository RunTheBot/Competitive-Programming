a = int(input())
b = int(input())

count = 1

while b >= 0:
    a, b = b, a-b
    count += 1

print(count)
