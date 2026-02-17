

def max_and_min(lst):
  max_val = max(lst)
  min_val = min(lst)
  return max_val, min_val

my_list = [4, 8, 1, 7, 5]
results = max_and_min(my_list)
print(f'Largest and smallest values in the list are {results}.')

