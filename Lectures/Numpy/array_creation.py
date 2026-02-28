
import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([[1, 2, 3], [4, 5, 6]])
b1 = np.array([[1, 2, 3],[4, 5, 6]]) # This will raise an error because the input is not a list of lists
b2 = np.array([[1, 2, 3], [4, 5, 6]], float) # This is correct and will create a 2D array

print(a1)
print(a2)
print(b1)
print(b2)
