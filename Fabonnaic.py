n = int(input("Enter the number of terms: "))
a, b = 0, 1
if n <= 0:
    print("Error: Invalid input. Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence of 1 term:", a)
else:
    # print the first two terms
    print("Fibonacci sequence of", n, "terms:")
    print(a, b, end=" ")

    i = 2
    while i < n:
        c = a + b
        print(c, end=" ")

        a, b = b, c
        i += 1
