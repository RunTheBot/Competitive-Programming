def hex_to_dec(hex_str):
    decimal = 0
    power = 0
    
    power_of_16_str = ""
    sum_str = ""
    
    # Convert hex string to uppercase for consistency
    hex_str = hex_str.upper()
    # Process hex string from right to left
    for digit in reversed(hex_str):
        # Convert hex digit to decimal value
        if digit.isdigit():
            value = int(digit)
        else:
            value = ord(digit) - ord('A') + 10
            
        if value > 0:
            decimal += value * (16 ** power)
            power_of_16_str += f"{value}×16^{power} + "
            sum_str += f"{value * (16 ** power)} + "
        power += 1
        
    print(f"{power_of_16_str[:-3]} = {sum_str[:-3]} = {decimal}")
    
    return decimal

hex_to_dec(input("Enter a hexadecimal number: "))