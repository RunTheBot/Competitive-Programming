n = int(input())
string = ""

s = 0
t = 0

for i in range(n):
    string += input().lower()

s = string.count("s")
t = string.count("t")

if s >= t:
    print("French")
else:
    print("English")
