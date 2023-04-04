total_sum = 0

while True:
    num = int(input("Enter a positive integer (enter 0 to exit): "))
    if num == 0:
        break
    elif num > 100:
        print("Number greater than 100, not included in sum.")
        continue
    else:
        total_sum += num

print("The sum of all positive integers (excluding numbers greater than 100) entered is:", total_sum)
