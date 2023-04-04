num = int(input("Enter a positive integer: "))
if num <= 0:
    print("Error: Invalid input. Please enter a positive integer.")
else:
    print("Multiplication table of", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
