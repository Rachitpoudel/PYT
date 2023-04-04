num = float(input("Enter a number: "))
def positive_or_negative(num):
    """"
    Determines if a number is positive or negative.

    
        num (int or float): The number to check.

    
        str: "Positive" if num is greater than 0, "Negative" if num is less than 0, and "Zero" if num is equal to 0.
    """
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    

# Ask the user for a number


# Call the function and print the result
result = positive_or_negative(num)
print(f"The number {num} is {result}.")
print(positive_or_negative.__doc__)



def find_lowest_number(num1, num2):
    """
    A function that accepts two numbers and returns the lowest number.
    """
    if num1 < num2:
        return num1
    else:
        return num2

if __name__ == "__main__":
    """
    A program that accepts two numbers from the user and finds the lowest number.
    """
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    lowest_number = find_lowest_number(num1, num2)
    print(f"The lowest number is: {lowest_number}")





def is_divisible_by_two_and_three(num):
    """
    A function that accepts a number and returns True if the number is divisible by both 2 and 3, otherwise False.
    """
    if num % 2 == 0 and num % 3 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    """
    A program that accepts a number from the user and checks whether the number is divisible by both 2 and 3.
    """
    num = int(input("Enter a number: "))
    result = is_divisible_by_two_and_three(num)
    if result:
        print("The number is divisible by both 2 and 3.")
    else:
        print("The number is not divisible by both 2 and 3.")
