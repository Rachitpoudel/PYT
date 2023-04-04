q=0
i=0
f=0
while True:
    a=int(input('entwe a number:'))
    print('press 101 to end')
    if a==101:
        break
    elif a>0:
        q=q+1
    elif a<0:
        i=i+1
    elif a==0:
        f=f+1
    else:
        print("invalid input")

print(f"the number of positive number entered is {q}. The number of nrgative number entered is {i}. The number of zeros entered is {f}")