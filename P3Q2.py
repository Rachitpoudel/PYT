product = 1
while True:
    num = int(input("Enter an integer (enter 0 to exit): "))
    if num == 0:
        break
    product *= num
print("The product of all the integers entered is:", product)
