number1 = float(input())
number2 = float(input())
operation = input()
if operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '/':
    print('Division by 0!' if number2 == 0 else number1 / number2)
elif operation == '*':
    print(number1 * number2)
elif operation == 'mod':
    print('Division by 0!' if number2 == 0 else number1 % number2)
elif operation == 'pow':
    print(number1 ** number2)
else:
    print('Division by 0!' if number2 == 0 else number1 // number2)