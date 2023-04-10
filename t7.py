with open("example.txt",'r') as f:
    one_line = f.readline()
    multiple_line = f.readlines()
    print("single line==>\n",one_line)
    print("multiple lines",multiple_line)
