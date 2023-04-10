def convert_to_single_integer(int_list):
    """
    This function takes in a list of multiple integers and returns a single integer.
    """
    single_integer = 0
    for integer in int_list:
        single_integer = single_integer * 10 + integer
    return single_integer
int_list = [11, 33, 50]
single_integer = convert_to_single_integer(int_list)
print(single_integer)
