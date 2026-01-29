from cmath import sqrt
import random

answer = input('pick a number! ')
user_num = float(answer)
third = user_num/3
print('here is a third:', third)

pi = 3.141592653589793
print(f'pi = {pi:.2f}')

#+ addition
9 + 4 
#− subtraction 9 - 4 5
#∗ multiplication 9 * 4 36
#/ division 9 / 4 2.25 result is a float
#// floor 9 // 4 2 integer division
#% modulus 9 % 4 1 remainder aft8er division
#∗∗ exponent 9 ** 4 6561

left = int(input('How many left socks?'))
right = int(input('How many right socks?'))
print(f'Number of unmatched socks: {abs(left - right)}')

##sqrt(x) square root of x
#exp(x) exponential function e x
#log(x) natural logarithm of x
#log10(x) base 10 logarithm of x
#sin(x), cos(x), tan(x) trigonometric functions, x in radians

print(sqrt(2))

meeting_time = random.randint(5, 9)
print(f'Let\'s meet tomorrow at {meeting_time} pm.')


area = float(input('Area of the square? '))
side = sqrt(area)
print(f'Side length of the square is {side}')
