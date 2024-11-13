# CCC '21 S3 - Lunch Concert
# DMOJ: https://dmoj.ca/problem/ccc21s3

def total_walking_time(v, friends):
    total_time = 0
    for friend in friends:
        P, W, D = friend
        distance = abs(P - v)
        if distance > D:
            total_time += (distance - D) * W
    return total_time

# Input processing
n = int(input())  
friends = []

for _ in range(n):
    P, W, D = map(int, input().split())
    friends.append((P, W, D))

# Find the minimum total walking time

min_position = min(friend[0] for friend in friends)
max_position = max(friend[0] for friend in friends)

low, high = min_position, max_position
ans = float('inf')

while low <= high:
    mid = (low + high) // 2
    centre = total_walking_time(mid, friends)
    left = total_walking_time(mid - 1, friends)
    right = total_walking_time(mid + 1, friends)
    
    ans = min(ans, centre)
    
    if left < right:
        high = mid - 1
    else:
        low = mid + 1

print(ans)