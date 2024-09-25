# Amplitude Hackathon Summer '24 Practice Problem 1 - Jeffrey's Favorite Integer
# DMOJ: https://dmoj.ca/problem/ampl2024spracticep1

# Binary Search
# 1 to 100
low = 1
high = 100
while True:
    mid = (low + high) // 2
    print(mid)
    response = input()
    if response == "CORRECT":
        break
    elif response == "LESS":
        high = mid - 1
    else:
        low = mid + 1

