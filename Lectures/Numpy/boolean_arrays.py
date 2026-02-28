

import numpy as np

a = np.array([[2,5],[7,4]])
is_even = a % 2 == 0
low = a < 3
middle = (a > 3) & (a < 6)
high = a > 6

print(is_even, end=' ')
print(low, end=' ')  
print(middle, end=' ')
print(high, end='')