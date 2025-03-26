def bin_to_hex(binary):
    # Ensure the binary length is multiple of 4 by padding with zeros
    while len(binary) % 4 != 0:
        binary = '0' + binary
    
    print(f"Input binary: {binary}")
    print("Separating into groups of 4:")
    
    # Separate into groups of 4
    groups = []
    for i in range(0, len(binary), 4):
        group = binary[i:i+4]
        groups.append(group)
        print(f"Group: {group}")
    
    # Convert each group to hex
    hex_result = ''
    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    
    print("\nConverting each group to hex:")
    for group in groups:
        hex_digit = hex_map[group]
        print(f"Binary {group} = Hex {hex_digit}")
        hex_result += hex_digit
    
    print(f"\nFinal hex result: {hex_result}")
    return hex_result

# Example usage
binary = input("Enter a binary number: ").strip().replace(" ", "")
bin_to_hex(binary)