
matrix = [[1,2,3], ['a','b','c']] # start with creating an empty list
for i in range(1, 4):       # let i take the values 1, 2, 3
  matrix.append([i])         # add a new row (a new empty list in the list)
  for j in range(1, 6):     # let j take the values 1, 2, 3, 4, 5
    matrix[-1].append(i*j)  # add to the end of the (so far) last row: i*j
print(matrix)