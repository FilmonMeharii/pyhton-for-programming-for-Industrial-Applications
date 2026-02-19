user_data = input('Give some values: ')  # e.g. 7 3 -5 0 2 -1 8 -3

# Convert input to a list of integers
numbers = [int(x) for x in user_data.split()]

# Filter only non-negative numbers
positiva = [num for num in numbers if num >= 0]

print(positiva)  # [7, 3, 0, 2, 8]