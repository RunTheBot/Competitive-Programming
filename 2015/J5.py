words = []
while True:
    word = input()
    if word == "X":
        break
    else:
        words.append(word)

for word in words:
    while True:
        if "ANA" in word or "BAS" in word:
            word = word.replace("ANA", "A")
            word = word.replace("BAS", "A")
        else:
            break
    if word == "A":
        print("YES")
    else:
        print("NO")
