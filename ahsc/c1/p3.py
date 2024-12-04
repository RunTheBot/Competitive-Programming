n = int(input())
answer_key = input().strip()
williams_answers = input().strip()


prefix_sum = [0] * (n + 1)
suffix_sum = [0] * (n + 1)

for i in range(n - 1):
    if williams_answers[i] == answer_key[i]:
        prefix_sum[i + 1] = prefix_sum[i] + 1
    else:
        prefix_sum[i + 1] = prefix_sum[i]

for i in range(n - 1, 0, -1):
    if williams_answers[i - 1] == answer_key[i]:
        suffix_sum[i - 1] = suffix_sum[i] + 1
    else:
        suffix_sum[i - 1] = suffix_sum[i]

max_score = 0
for i in range(n):
    max_score = max(max_score, prefix_sum[i] + suffix_sum[i])

print(max_score)