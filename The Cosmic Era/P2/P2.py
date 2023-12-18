min = 1
max = 2 * (10 ** 9)

while True:
    guess = (min + max) >> 1
    print(guess)
    result = input()
    if result == "FLOATS":
        max = guess - 1
    elif result == "SINKS":
        min = guess + 1
    else:
        break
