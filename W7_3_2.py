with open("Datafile.txt", "r") as f_in, open("example.txt", "w") as f_out:
    lines = f_in.readlines () 
for i in range(len(lines)) :
    f_out.write(lines[1])
