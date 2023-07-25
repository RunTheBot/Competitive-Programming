expression = input().replace("^", "**").split()

while len(expression) > 1:
    operator = expression[2]
    if operator == '+':
        expression[0] = float(expression[0]) + float(expression[1])
        expression.pop(1)
        expression.pop(1)
    elif operator == '-':
        expression[0] = float(expression[0]) - float(expression[1])
        expression.pop(1)
        expression.pop(1)
    elif operator == '*':
        expression[0] = float(expression[0]) * float(expression[1])
        expression.pop(1)
        expression.pop(1)
    elif operator == '/':
        expression[0] = float(expression[0]) / float(expression[1])
        expression.pop(1)
        expression.pop(1)
    elif operator == '%':
        expression[0] = float(expression[0]) % float(expression[1])
        expression.pop(1)
        expression.pop(1)
    elif operator == '**':
        expression[0] = float(expression[0]) ** float(expression[1])
        expression.pop(1)
        expression.pop(1)

print(expression[0])
