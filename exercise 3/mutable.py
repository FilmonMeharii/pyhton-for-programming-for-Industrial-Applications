lst = [3, 0, -2, 1, 1, -1, -2, 3, 2, 3, 0]
for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0
print(lst)
