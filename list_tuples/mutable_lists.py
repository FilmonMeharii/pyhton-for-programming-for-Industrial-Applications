

lst = [0, 0, 0, 0, 0, 0, 0]
lst[1] = 9 # [0, 9, 0, 0, 0, 0, 0]
lst[3:6] = [8, 7, 6] 


lst = [1, 2, 3, 4, 5]
for i in range(len(lst)):
    lst[i] *= 2
print(lst)