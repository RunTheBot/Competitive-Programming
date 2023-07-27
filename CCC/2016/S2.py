qType = input()
total = int(input())
dmoj = map(int, input().split())
dmoj = sorted(dmoj)
peg = map(int, input().split())
peg = sorted(peg)

if qType == "1":
    print(sum([max(dmoj[i], peg[i]) for i in range(total)]))
else:
    peg = peg[::-1]
    print(sum([max(dmoj[i], peg[i]) for i in range(total)]))
