cities = input().split()
cities = list(map(int, cities))
cities.insert(0, 0)
for x in range(5):
    out = []
    for y in range(5):
        if x == y:
            out.append("0")
        elif x < y:
            out.append(str(sum(cities[slice(x+1, y+1)])))
        else:
            out.append(str(sum(cities[slice(y+1, x+1)])))
    print(" ".join(out))
