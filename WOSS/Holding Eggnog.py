# WOSS Dual Olympiad 2023 Team Round P2: Holding Eggnog
# DMOJ: https://dmoj.ca/problem/wossoly23team2

n = int(input())

building_heights = list(map(int, input().split()))
stack = []
total_eggnog = 0

for current_index in range(len(building_heights)):
    while stack and building_heights[current_index] > building_heights[stack[-1]]:
        valley_index = stack.pop()
        if not stack:
            break
        left_index = stack[-1]
        width = current_index - left_index - 1
        height = min(building_heights[current_index], building_heights[left_index]) - building_heights[valley_index]
        total_eggnog += width * height

    stack.append(current_index)

print(total_eggnog)
