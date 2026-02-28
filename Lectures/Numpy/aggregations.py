
import numpy as np

arr = np.array([6,9,5,7])
min_val = np.min(arr)
min_idx = np.argmin(arr)

total_1 = sum(arr)
total_2 = np.sum(arr)
total_3 = arr.sum()

print(total_1)
print(total_2)
print(total_3)