

def my_max(list):
    max_value = list[0]
    for item in list:
        if item > max_value:
            max_value = item
    return max_value

def arg_max(list):
    max_value = list[0]
    max_index = 0
    for index, item in enumerate(list):
        if item > max_value:
            max_value = item
            max_index = index
    return max_index

l = [1, 3, 2, 5, 4]
m = my_max(l)
print("Max value:", m)