while True:
    num1 = input("Enter first number: ")
    if num1 == 'q':
        break
    num2 = input("Enter second number: ")
    if num2 == 'q':
        break
    op = input("Enter operation (+, -, *, /): ")
    if op == 'q':
        break
    
    num1 = float(num1)
    num2 = float(num2)
    
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print("Invalid operation")
        continue
    
    print("Result: ", result)
