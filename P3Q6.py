string = input("Enter a string: ")
vowels = "aeiou"
count = 0

for char in string:
    if char in vowels:
        count += 1
print("The number of vowels in the string is:", count)
