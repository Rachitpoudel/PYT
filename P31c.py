total_sum = 0
num = 100

while True:
    if num > 200:
        break
    elif num % 2 != 0:
        num += 1
        continue
    else:
        total_sum += num
        num += 2

print("The sum of all even numbers between 100 and 200 is:", total_sum)
