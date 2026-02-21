

def swap(a, b):
    a , b = b, a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
swap(x, y)
print(f"First number: {x}, Second number: {y}") 


def minimum(a, b):
    if a>b:
        return b            
    return a