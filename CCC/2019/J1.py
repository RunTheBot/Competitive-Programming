for i in range(int(input())):
    text = input()
    output = ""
    count = 1
    index = 0
    char = ""
    while True:
        try:
            if text[index] != char:
                output += str(count) + " " + char + " " if count > 1 else ""
                char = text[index]
                index += 1
                count = 1
            else:
                index += 1
                count += 1
        except IndexError:
            output += str(count) + " " + char
            print(output)
            break
        except Exception as error:
            print(error)
            break
