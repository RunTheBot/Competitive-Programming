# Ceser Cypher

n, shifts = map(int, input().split())

for i in range(n):
    # decode the string
    string = input()
    decoded = ""
    for char in string:
        if char == " ":
            decoded += " "
        else:
            decoded += chr((ord(char) - 97 - shifts) % 26 + 97)
    print(decoded)

