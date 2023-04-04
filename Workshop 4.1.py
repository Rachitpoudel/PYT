def british_grade(percentage):
    """
    A function that accepts a percentage and returns the corresponding grade according to the British mark sheet.
    """
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'E'

if __name__ == "__main__":
    """
    A program that accepts a percentage from the user and displays the corresponding grade according to the British mark sheet.
    """
    percentage = float(input("Enter your percentage: "))
    grade = british_grade(percentage)
    print(f"Your grade is: {grade}")




def is_leap_year(year):
    """
    A function that checks whether a year is a leap year or not.

    Leap years are those which are divisible by 4 but not by 100, except for years that are divisible by 400.

    Args:
    year (int): The year to be checked

    Returns:
    bool: True if the year is a leap year, False otherwise
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    """
    A program that checks whether a year is a leap year or not.
    """
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")



def check_voting_eligibility(age):
    """
    A function that checks whether a person is eligible for voting or not based on their age.
    """
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote yet."

if __name__ == "__main__":
    """
    A program that checks whether a person is eligible for voting or not based on their age.
    """
    age = int(input("Enter your age: "))
    eligibility = check_voting_eligibility(age)
    print(eligibility)
