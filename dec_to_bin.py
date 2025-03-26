def decimal_to_binary_with_steps(decimal):
    if decimal == 0:
        return "0000"
    
    original = decimal
    binary = ""
    steps = []
    
    while decimal > 0:
        remainder = decimal % 2
        quotient = decimal // 2
        steps.append(f"{decimal} ÷ 2 = {quotient} remainder {remainder}")
        binary = str(remainder) + binary
        decimal = quotient
    
    # Add leading zeros to make length multiple of 4
    while len(binary) % 4 != 0:
        binary = "0" + binary
    
    # Separate into groups of 4
    formatted_binary = " ".join([binary[i:i+4] for i in range(0, len(binary), 4)])
    
    # Print the steps and result
    print(f"Converting {original} to binary:")
    for step in steps:
        print(step)
    print(f"\nFinal binary result: {formatted_binary}")
    return formatted_binary

# Example usage
number = int(input("Enter a decimal number: "))
decimal_to_binary_with_steps(number)