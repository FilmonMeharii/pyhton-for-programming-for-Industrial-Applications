import numpy as np


a = np.array([[2,5],[7,4]])
is_even = a % 2 == 0
even_elements = a[is_even]
b = a[(a > 3) & (a < 6)]