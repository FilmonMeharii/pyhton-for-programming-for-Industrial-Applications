

import numpy as np

a= np.array([4, 6, 7, 9])
i1 = np.array([2, 1, 3])
a1 = a[i1] # [7 6 9]
i2 = np.array([[2, 1], [3, 0]])
a2 = a[i2] # [[7 6], [9 4]]


b = np.array([[8, 6, 9], [4, 5, 3]])
row, col = [1, 0], [0, 2]
b1 = b[row, col]