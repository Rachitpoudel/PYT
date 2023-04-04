def status():
    """A student enters the number of college credits earned.
    if greater than or equal to 60, 'Junior Status' is displayed; if greater than or equal to 30, 'Sophomore Status' is displayed; else, 'Freshman Status' is displayed."""
    totalCredit = int(input("enter your total credit: "))

    if totalCredit >= 90:
        print("Senior Status")
    elif totalCredit >= 60:
        print("Junior Status")
    elif totalCredit >= 30:
        print("Sophomore Status")
    else:
        print("Freshman Status")
status()