

def add_elementwise(lst1, lst2):
    assert len(lst1) == len(lst2), "The lists do not have the same length!"
    return [a + b for a, b in zip(lst1, lst2)]


def add_numerical(lst):
    total = 0
    for item in lst:
        try:
            total += item
        except TypeError:
            continue
    return total


# Only runs if this file is executed directly
if __name__ == "__main__":
    lst1 = [1, 1, 2, 2, 3, 3]
    lst2 = [0, 1, 2, 3, 4, 5]
    the_sum = add_elementwise(lst1, lst2)
    print(the_sum)  # [1, 2, 4, 5, 7, 8]

    L1 = [1, 1, 1, 4, 4]
    L2 = [3, 5, 6, 0]
    total = add_elementwise(L1, L2)  # AssertionError

    l1 = [1, 2, 3, 4, 5, 'monkey', 6.0]
    the_sum = add_numerical(l1)
    print(the_sum)  # 21.0