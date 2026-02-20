

from find_all_occurrences import find_all_positions
from  list_functions import arg_min 

values = [14, 24, 10, 15, 10]
min_pos = arg_min(values)  #2    
print(f'Minimum value is {values[min_pos]} at index {min_pos}')


positions = find_all_positions(values, 10)

print(f"The smallest number is found on position {min_pos}.")
print(f"The given value is found on positions {positions}")