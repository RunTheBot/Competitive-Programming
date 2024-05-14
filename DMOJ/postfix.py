
expression = input().split()

stack = []

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '^': lambda a, b: a ** b,
    '%': lambda a, b: a % b
}

for char in expression:
    if char.isdigit():
        # print("char", char)
        stack.append(int(char))
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(operations[char](a, b))

print(stack[0])
