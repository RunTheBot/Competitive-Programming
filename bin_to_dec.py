def bin_to_dec(binary_str):
    decimal = 0
    power = 0
    
    power_of_two_str = ""
    sum_str = ""
    
    # Process binary string from right to left
    for digit in reversed(binary_str):
        if digit == '1':
            decimal += 2 ** power
            power_of_two_str += f"2^{power} + "
            sum_str += f"{2 ** power} + "
        power += 1
    print(f"{power_of_two_str[:-3]} = {sum_str[:-3]} = {decimal}")
    
    return decimal

bin_to_dec(input("Enter a binary number: "))
