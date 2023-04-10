def insert_string_at_beginning(lst, string):
    new_list = [string + str(item) for item in lst]
    return new_list
my_list = [1, 2, 3, 4]
my_string = "emp"
new_list = insert_string_at_beginning(my_list, my_string)
print(new_list)
