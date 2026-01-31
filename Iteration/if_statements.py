

c = float(input('Enter temperature in Celsius: '))
f= c * 9/5 + 32
print(f'Temperature in Fahrenheit: {f}')


c = float(input('Enter temperature in Celsius: '))
if c >= -273.15:
    f= c * 9/5 + 32
    print(f'Temperature in Fahrenheit: {f:.2f}')
    

n=int(input('Number: ' ))
if n> 0:
    n =-n
print(f'absolute value is: {n}')


c = float(input('Enter temperature in Celsius: '))
if c >= -273.15:
    f= c * 9/5 + 32
    print(f'Temperature in Fahrenheit: {f:.2f}')
else: print('Invalid temperature: below absolute zero!')