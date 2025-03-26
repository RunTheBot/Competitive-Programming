# "1101 x 10 ="

# do the multiplication binary and decimal
# binary1, binary2 = input()[0:-2].split(" x ")
binary1, binary2 = input().split(" * ")

# Convert to integers
num1 = int(binary1, 2)
num2 = int(binary2, 2)

# Multiply
result_decimal = num1 * num2
result_binary = bin(result_decimal)[2:]  # Remove '0b' prefix

print(f"{binary1} x {binary2} = {result_binary} (binary)")
print(f"{num1} x {num2} = {result_decimal} (decimal)")