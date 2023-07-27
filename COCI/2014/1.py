string = input()

fingers = [0] * 8

for char in string:
    if char == "1" or char == "Q" or char == "A" or char == "Z":
        fingers[0] += 1
    if char == "2" or char == "W" or char == "S" or char == "X":
        fingers[1] += 1
    if char == "3" or char == "E" or char == "D" or char == "C":
        fingers[2] += 1
    if char == "4" or char == "R" or char == "F" or char == "V" or char == "5" or char == "T" or char == "G" or char == "B":
        fingers[3] += 1
    if char == "6" or char == "Y" or char == "H" or char == "N" or char == "7" or char == "U" or char == "J" or char == "M":
        fingers[4] += 1
    if char == "8" or char == "I" or char == "K" or char == ",":
        fingers[5] += 1
    if char == "9" or char == "O" or char == "L" or char == ".":
        fingers[6] += 1
    if char == "0" or char == "P" or char == ";" or char == "/" or char == "-" or char == "[" or char == "'" or char == "=" or char == "]":
        fingers[7] += 1

for finger in fingers:
    print(finger)
