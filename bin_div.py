# "1101 / 10 ="

# do the division binary and decimal
binary2, binary1 = input().split(" / ")

# Convert to integers
num1 = int(binary1, 2)
num2 = int(binary2, 2)

# Divide and get remainder
quotient = num1 // num2
remainder = num1 % num2
quotient_binary = bin(quotient)[2:]  # Remove '0b' prefix
remainder_binary = bin(remainder)[2:]  # Remove '0b' prefix

print(f"{binary1} / {binary2} = {quotient_binary} r{remainder_binary} (binary)")
print(f"{num1} / {num2} = {quotient} r{remainder} (decimal)")