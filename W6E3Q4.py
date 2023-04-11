def filter_by_vowel(strings_set):
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    filtered_set = set()
    for string in strings_set:
        if string[0].lower() in vowels:
            filtered_set.add(string)
    return filtered_set
strings_set = {'Apple', 'Banana', 'Orange', 'Car', 'Egg'}
filtered_set = filter_by_vowel(strings_set)
print(filtered_set)
