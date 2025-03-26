def hex_to_bin(hexadecimal):
    # Remove any spaces and convert to uppercase
    hexadecimal = hexadecimal.strip().replace(" ", "").upper()
    
    print(f"Input hexadecimal: {hexadecimal}")
    print("Converting each hex digit to binary:")
    
    # Map for hex to binary conversion
    hex_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    binary_result = ''
    for digit in hexadecimal:
        if digit not in hex_map:
            raise ValueError(f"Invalid hexadecimal digit: {digit}")
        binary = hex_map[digit]
        print(f"Hex {digit} = Binary {binary}")
        binary_result += binary
    
    print(f"\nFinal binary result: {binary_result}")
    return binary_result

# Example usage
hexadecimal = input("Enter a hexadecimal number: ")
hex_to_bin(hexadecimal)