

lst = [0, 0, 0, 0, 0, 0, 0]
lst[1] = 9 # [0, 9, 0, 0, 0, 0, 0]
lst[3:6] = [8, 7, 6] 


lst = [1, 2, 3, 4, 5]
for i in range(len(lst)):
    lst[i] *= 2
print(lst)


#iterating over a the elements of a list

lst = [1, 2, 3, 4, 5]
for item in lst:
    if item % 2 == 0:
        print(item, end=' ')


tpl = (8, -4, 10, 3, -7, -2)
counter = 0
for i in range(len(tpl)):
    if tpl[i] > 0:
        counter += tpl[i]
print(counter)