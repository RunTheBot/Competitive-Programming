# Open words_alpha.txt

with open('words_alpha.txt', 'r') as file:
    words = file.readlines()

    for word in words:
        word = word[:-2]
        # print(word)

        value = 0

        for char in word:
            value += ord(char) - 96

        if value == 100:
            print(word)


