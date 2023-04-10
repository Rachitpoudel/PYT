def strings_with_a(list_of_strings):
    new_list = []
    for string in list_of_strings:
        if 'a' in string:
            new_list.append(string)
    return new_list
list_of_strings = ["apple", "banana", "cherry", "date", "elderberry", "fig" ,"Rachit" ,"America"]

strings_with_a_list = strings_with_a(list_of_strings)

print(strings_with_a_list) 
