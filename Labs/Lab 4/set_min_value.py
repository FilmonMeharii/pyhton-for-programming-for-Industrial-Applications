
def set_min_value(lst, min_value):
    for i in range(len(lst)):
        if lst[i] < min_value:
            lst[i] = min_value

lst = [4, -2, 0, 3, 7]
set_min_value(lst, 2)
print(lst)              # [4, 2, 2, 3, 7]

lst = [-13, 5, -6, 9, 0]
set_min_value(lst, -3)
print(lst)              # [-3, 5, -3, 9, 0]

lst = [8, 9, 13, 6, 5]
set_min_value(lst, 1)
print(lst)              # [8, 9, 13, 6, 5]