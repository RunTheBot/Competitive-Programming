# Amplitude Hackathon Summer '24 Problem 2 - Feature Requests
# DMOJ: https://dmoj.ca/problem/ampl2024sp2

n = int(input())

features = dict()

for i in range(n):
    count, *data = input().split()
    featureRequests = data

    for feature in featureRequests:
        if feature in features:
            features[feature] += 1
        else:
            features[feature] = 1

for key, value in sorted(features.items(), key=lambda item: (-item[1], item[0])):
    print(key, value)
