def double_list(lst):
    """
    Double each element in a list.
    """
    for ind in range(lst, 0, -1):
        lst[ind] = lst[ind] * 2
    return lst


first_list = [1, 2, 3]
second_list = double_list(first_list)

print(f"Double each element in {first_list} and get {second_list}")
