num = int(input("Enter a number: "))
smallest_digit = 9
while num > 0:
    digit = num % 10
    if digit < smallest_digit:
        smallest_digit = digit
    num //= 10
print("The smallest digit in the number is:", smallest_digit)
