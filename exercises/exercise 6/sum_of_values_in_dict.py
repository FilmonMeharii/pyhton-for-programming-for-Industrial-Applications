

def sam_values(d):
    total = 0
    for value in d.values():
        total += value
    return total

d = {'a': 2, 'o': 7, 'u': 10, 'å': 5, 'e': 2, 'i': 1, 'y': 9, 'ä': 6, 'ö': 3}
the_sum = sam_values(d)
print(f"The sum of the values in the dictionary is: {the_sum}")