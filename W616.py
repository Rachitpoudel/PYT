num_list = input("Enter a list of integers (separated by spaces): ").split()
num_list = [int(num) for num in num_list]
for i in range(len(num_list)):
    if num_list[i] > 100:
        num_list[i] = 'over'
print(num_list)
