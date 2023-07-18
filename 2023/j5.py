z = input()
h = int(input())
w = int(input())
wl = len(z)
o = []
t = []

for i in range(0, h):
    o.append(input().split(" "))


def look(l, x, y):
    nx, ny = x + 1, y
    check(nx,ny,l)
    print(1)
    nx, ny = x + 1, y + 1
    check(nx,ny,l)
    print(2)
    nx, ny = x + 1, y - 1
    check(nx,ny,l)
    print(3)
    nx, ny = x - 1, y + 1
    check(nx,ny,l)
    print(4)
    nx, ny = x - 1, y - 1
    check(nx,ny,l)
    print(5)
    nx, ny = x - 1, y
    check(nx,ny,l)
    print(6)
    nx, ny = x, y + 1
    check(nx,ny,l)
    print(7)
    nx, ny = x, y - 1
    check(nx,ny,l)
    print(8)

def check(x,y,l):
    try:
        if o[y][x] == z[l]:
            nlook(l + 1, x, y)
    except:
        return

def nlook(l, x, y, t2=t):
    if l < wl - 1:
        look(l+1, x, y)
    else:
        t.append("")

for y in range(0, h):
    for x in range(0, w):
        if o[y][x] == z[0]:
            look(1, x, y)

print(len(t)+1)
