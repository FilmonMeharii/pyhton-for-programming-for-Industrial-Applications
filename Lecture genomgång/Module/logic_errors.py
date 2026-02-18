

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4, 5])) # True - as expected
print(is_sorted([3, 4, 2, 5, 1])) # False - as expected
print(is_sorted([1, 2, 2, 3, 5])) # True - as expected