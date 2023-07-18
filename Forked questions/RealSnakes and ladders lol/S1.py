place = 1
while True:
    move = int(input())
    if move == 0:
        print("You Quit!")
        break

    movesTillEnd = 100-place

    place = 100-abs(movesTillEnd - move)

    if place == 54:
        place = 19
    elif place == 90:
        place = 48
    elif place == 99:
        place = 77
    elif place == 9:
        place = 34
    elif place == 40:
        place = 64
    elif place == 67:
        place = 86

    print("You are now on square", place)
