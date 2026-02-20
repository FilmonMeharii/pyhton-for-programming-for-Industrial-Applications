

from queue import Empty


def arg_min(lst):
    if not lst:
        return ValueError('Empty list')
    min_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
    return min_index

#values = [6,3,4,8,1,5]
#min_pros = arg_min(values)
values = [14, 24, 10, 15, 10]
min_pos = arg_min(values)     # 2
print(f'Minimum value is {values[min_pos]} at index {min_pos}')
