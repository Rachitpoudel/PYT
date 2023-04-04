def leap_year():
    """This function is defined to figure out if the given year is a leap year or not"""
    year = int(input("enter the year"))
    if year % 4 ==0 and (year % 100 !=0 or year % 400 == 0):
        print(year,"it is leap year")
    else:
     print(year, "is not leap year")

leap_year()