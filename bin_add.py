def binary_operation_table(a, b, operation='+'):
    # Convert numbers to binary strings of equal length
    max_len = max(len(bin(abs(a))[2:]), len(bin(abs(b))[2:]))
    if operation == '-':
        # For subtraction, we need one more bit if b is negative
        max_len += 1 if b < 0 else 0
    
    bin_a = bin(a)[2:].zfill(max_len)
    bin_b = bin(b)[2:].zfill(max_len)
    
    if operation == '+':
        # Addition logic
        carry = 0
        result = ''
        carry_string = ''
        
        for i in range(max_len-1, -1, -1):
            bit_sum = int(bin_a[i]) + int(bin_b[i]) + carry
            carry = bit_sum // 2
            result = str(bit_sum % 2) + result
            carry_string = str(carry) + carry_string
        
        if carry:
            result = '1' + result
            carry_string = ' ' + carry_string
            
        # Display the addition table
        print("\033[93m" + carry_string.rjust(max_len+1) + "\033[0m")  # Yellow color for carry
        print(bin_a.rjust(max_len+1))
        print(bin_b.rjust(max_len+1))
        print('_' * (max_len+1))
        print(result.rjust(max_len+1))
        print(f"\n{a} + {b} = {a+b}")
        
    else:  # Subtraction
        # For subtraction, we'll use two's complement
        result = bin((a - b) & ((1 << max_len) - 1))[2:].zfill(max_len)
        print(bin_a.rjust(max_len+1))
        print(bin_b.rjust(max_len+1))
        print('_' * (max_len+1))
        print(result.rjust(max_len+1))
        print(f"\n{a} - {b} = {a-b}")

# Parse input
expression = input("").replace(" ", "")
if '+' in expression:
    a, b = map(lambda x: int(x, 2), expression.split('+'))
    binary_operation_table(a, b, '+')
elif '-' in expression:
    a, b = map(lambda x: int(x, 2), expression.split('-'))
    binary_operation_table(a, b, '-')

