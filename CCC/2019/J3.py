for i in range(int(input())):
    text = input()
    output = []
    count = 1
    CurrChar = ""

    for char in text:
        if char != CurrChar:
            output.append(str(count))
            output.append(CurrChar)
            CurrChar = char
            count = 1
        else:
            count += 1


    output.append(str(count))
    output.append(CurrChar)

    output.pop(0)
    output.pop(0)

    print(" ".join(output))
