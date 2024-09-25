# Amplitude Hackathon Summer '24 Problem 3 - Mike's Unlocked Laptop
# DMOJ: https://dmoj.ca/problem/ampl2024sp3

# Mike's password will only consist of uppercase letters, lowercase letters, and digits. The length of Mike's password will be between 1,50

# Because Mike's laptop is in debugging mode, when Nick guesses a password, if it is incorrect, Mike's laptop will report the length of the longest common substring between Nick's guess and Mike's true password.

chars = [chr(i) for i in range(33, 127)]

# False: brute force appending at end of password
# True: brute force appending at start of password
mode = False

password = ""

prevBest = 0

done = False
while not done:
    for char in chars:
        if mode:
            guess = char + password
        else:
            guess = password + char
        print(guess)
        response = int(input())
        if response > prevBest:
            password = guess
            prevBest = response
            break
        elif response == -1:
            done = True
            break
    else:
        mode = not mode
