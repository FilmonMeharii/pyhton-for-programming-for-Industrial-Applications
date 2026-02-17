integers = input('Input a series of integers, separated by spaces: ')
target = int(input('Input a target value: '))

integers_list = [int(x) for x in integers.split()]

closest = integers_list[0]
min_distance = abs(closest - target)

for num in integers_list:
    distance = abs(num - target)
    if distance < min_distance:
        closest = num
        min_distance = distance

print(f'Closest: {closest}')