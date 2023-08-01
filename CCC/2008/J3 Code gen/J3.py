import json
# 2d array of GPS Text Entry

keypad = [['A', 'B', 'C', 'D', 'E', 'F'],
            ['G', 'H', 'I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P', 'Q', 'R'],
            ['S', 'T', 'U', 'V', 'W', 'X'],
            ['Y', 'Z', ' ', '-', '.', 'ENTER']]

object = {}

for row in range(len(keypad)):
    for col in range(len(keypad[row])):
        object[keypad[row][col]] = (row, col)

json.dump(object, open("keypad.json", "w"))

distObject = {}

for char in object:
    distObject[char] = {}
    for otherChar in object:
        # calculate distance
        distObject[char][otherChar] = abs(object[char][0] - object[otherChar][0]) + abs(object[char][1] - object[otherChar][1])

json.dump(distObject, open("distObject.json", "w"))
