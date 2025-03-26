"""It's christmas morning! Time to open the gifts under the christmas tree.

You are given 
N
 gifts, the 
i
t
h
 gift initially having a happiness value of 
h
i
 
(
1
≤
i
≤
N
)
. Some gifts may have a positive happiness value, while others might have a negative happiness value! (or zero, for that matter).

In one move, you can either use your magic powers to flip the sign of one of the gift's happiness values OR you can open a gift. Your final score is the sum of the happiness values of all the gifts you open. If you don't open any gifts, your score is 
0
.

What is the maximum happiness score you can achieve in 
K
 moves or less?"""


# N, K = map(int, input().split())

# gifts = list(map(int, input().split()))

# # First, sort gifts by absolute value in descending order with their indices
# gifts_with_idx = [(abs(x), x, i) for i, x in enumerate(gifts)]
# gifts_with_idx.sort(reverse=True)

# # Initialize variables
# best_score = 0
# n_moves = K

# # Try flipping up to min(K, number of negative values) negative values
# # starting with those having largest absolute values
# for flips in range(min(K + 1, sum(1 for x in gifts if x < 0) + 1)):
#     # Make a copy of original gifts
#     current_gifts = gifts.copy()
#     moves_left = K - flips
    
#     # Flip the 'flips' largest negative numbers
#     flips_used = 0
#     for _, orig_val, idx in gifts_with_idx:
#         if flips_used >= flips:
#             break
#         if current_gifts[idx] < 0:
#             current_gifts[idx] = -current_gifts[idx]
#             flips_used += 1
    
#     # Now take the largest positive numbers we can with remaining moves
#     score = sum(sorted(current_gifts, reverse=True)[:moves_left])
#     best_score = max(best_score, score)

# print(best_score)



# Read input
N, K = map(int, input().split())
gifts = list(map(int, input().split()))

pos = sorted([x for x in gifts if x > 0], reverse=True)
neg = sorted([abs(x) for x in gifts if x < 0], reverse=True)

pos_psa = [0]
neg_psa = [0]

for p in pos:
    pos_psa.append(pos_psa[-1] + p)
for n in neg:
    neg_psa.append(neg_psa[-1] + n)

max_score = 0

for x in range(min(K + 1, len(pos) + 1)):
    moves_left = K - x
    y = min(moves_left // 2, len(neg))
    
    score = pos_psa[x] + neg_psa[y]
    max_score = max(max_score, score)

print(max_score)