raws = 6 

for i in range(raws-1):
    for j in range(raws-i-1):   
     print(' ', end= ' ')
    for j in range(2*i*1):
        print("*", end= ' ')
    print()  