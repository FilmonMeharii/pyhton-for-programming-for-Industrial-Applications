
i = 0
while i < 10:
    print(i, end=' ')
    i += 1    
print()  
for i in range(10):
    print(i, end=' ')  
print()    

i = 100
while i < 200:
    print(i, end=' ')
    i += 10 
print() 


for i in range(100, 200, 10):
    print(i, end=' ')
print() 

for i in range(200, 100, -10):
    print(i, end = ' ')
print()

n = 5
for i in range(n):
    for j in range(n):
        print( i+j, end = ' ')
    print()

for i in range(5):
    print(i)