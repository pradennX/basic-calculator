num1 = int(input('Enter first number: \n'))
num2 = int(input('Enter second number: \n'))
op = input('Enter Operator \n')

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 // num2)
else:
    print("invalid operator")