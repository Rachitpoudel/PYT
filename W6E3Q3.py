def filter_by_age(people_list):
    """
    This function takes in a list of dictionaries representing people with their age,
    and returns a new list of dictionaries with only the people over the age of 18.
    """
    filtered_list = []
    for person in people_list:
        if person['age'] > 18:
            filtered_list.append(person)
    return filtered_list
people_list = [{'name': 'Apil', 'age': 25}, {'name': 'Rabi', 'age': 17}, {'name': 'Aashish', 'age': 21}]
filtered_list = filter_by_age(people_list)
print(filtered_list)
