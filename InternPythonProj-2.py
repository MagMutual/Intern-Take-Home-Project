def n_list(n: int, lst: list = []):
    """
    Creates a n-length list of n.
    """
    for _ in range(n):
        lst.append(n)
    return lst


def extend_to_match(lst_a: list, lst_b: list):
    """
    Extend the length of lst_a to match the length of lst_b.
    """
    len_a = lst_a[0]
    len_b = lst_b[len(lst_b) - 1]
    while len_a < len_b:
        len_a = lst_a[0]
        len_b = lst_b[len(lst_b) - 1]

        lst_a = [lst_a[0]] + lst_a
        lst_a[0] = lst_a[0] + 1
    return lst_a


list_1 = n_list(5)
list_2 = n_list(10)
print(f"list_1: {list_1}")
print(f"list_2: {list_2}")
list_3 = extend_to_match(list_1, list_2)
print(f"list_3: {list_3}")
