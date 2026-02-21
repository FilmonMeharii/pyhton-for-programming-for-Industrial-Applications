

def avg(a, b):
    return (a + b) / 2 

x = int(input("Enter first number: "))
y = int(input("Enter second number: ")) 
res = avg(x, y)
print(f"The average of {x} and {y} is: {res}")


#call by value
def avg(a,b):
    return (a + b) / 2
result = avg(x, y)
print(f"The average of {x} and {y} is: {result}")