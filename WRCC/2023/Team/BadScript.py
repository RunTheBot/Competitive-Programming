xVal, n = map(int, input().split())

main = []

for i in range(n):
    main = main + input().replace(";", "\n").replace(":", ":\n").split("\n")

print(main)

for i in range(len(main)):
    main[i] = main[i].strip()

for i in range(len(main)):
    from ba