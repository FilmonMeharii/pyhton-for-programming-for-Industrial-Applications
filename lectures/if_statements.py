

c = float(input('Enter temperature in Celsius: '))
f= c * 9/5 + 32
print(f'Temperature in Fahrenheit: {f}')


c = float(input('Enter temperature in Celsius: '))
if c >= -273.15:
    f= c * 9/5 + 32
    print(f'Temperature in Fahrenheit: {f:.2f}')
    