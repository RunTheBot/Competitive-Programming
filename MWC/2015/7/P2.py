F, R = map(int, input().split())
apartments = [list(map(int, input().split())) for _ in range(F)]
Q = int(input())
questions = [list(map(int, input().split())) for _ in range(Q)]

prefixSums = []
for floor in apartments:
    prefix_sum = [0]
    for cd_count in floor:
        prefix_sum.append(prefix_sum[-1] + cd_count)
    prefixSums.append(prefix_sum)

for a, b, c in questions:
    total_cds = prefixSums[c - 1][b] - prefixSums[c - 1][a - 1]
    print(total_cds)
