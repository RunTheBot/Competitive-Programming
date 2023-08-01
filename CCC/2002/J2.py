# CCC '02 J2 - AmeriCanadian

while True:
    string = input()
    if string == "quit!":
        break
    else:
        if len(string) > 4 and not (string[-3] == "a" or string[-3] == "e" or string[-3] == "i" or string[-3] == "o" or string[-3] == "u"):
            print(string if not string.endswith("or") else string[:-2] + "our")
        else:
            print(string)

exit()
