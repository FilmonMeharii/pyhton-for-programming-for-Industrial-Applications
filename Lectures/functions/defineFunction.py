

def double_that(x):                     # function definition, x is a parameter
  return 2 * x                          # function body

number = int(input('Give a number: '))
double = double_that(number)            # function call, number is an argument
print(f'You say {number}. I say double that: {double}')