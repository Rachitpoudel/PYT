def grade():
    p=float(input('Enter the percentage :  '))
    if p>=0 and p<=39:
        print('Obtained grade is F')
    elif p>=40 and p<=42:
        print('obtained grade is E')
    elif p>=43 and p<=49:
        print('obtained grade is D')
    elif p>=50 and p<=59:
        print('obtained grade is C')
    elif p>=60 and p<=69:
        print('obtained grade is B')
    elif p>=70 and p<=100:
        print('obtained grade is A')
    else:
        print('invalid input')
grade()