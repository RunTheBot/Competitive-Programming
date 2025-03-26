def decimal_to_hex(decimal_num):
    if decimal_num == 0:
        return "0"
    
    hex_digits = "0123456789ABCDEF"
    steps = []
    result = ""
    num = decimal_num
    
    while num > 0:
        remainder = num % 16
        quotient = num // 16
        steps.append(f"{num} ÷ 16 = {quotient} remainder {remainder} ({hex_digits[remainder]})")
        result = hex_digits[remainder] + result
        num = quotient
    
    # Print all steps
    print(f"\nConverting {decimal_num} to hexadecimal:")
    for step in steps:
        print(step)
    print(f"\nFinal result: {decimal_num} in hexadecimal is {result}")
    
    return result

decimal_to_hex(int(input("Enter a decimal number: ")))