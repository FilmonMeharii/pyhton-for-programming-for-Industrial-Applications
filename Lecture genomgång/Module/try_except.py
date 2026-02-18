


try:
    user_data = input("Enter a number: ")
    number = float(user_data)
    print(f'Inverse: {1 / number}')
except ValueError:
    print(f'Invalid number: {user_data}')
except ZeroDivisionError:
    print(f'Zero has no inverse')

try:
    user_data = int(input("Enter a number: "))
    numer = float(user_data)
    print(f'Inverse: {1/numer}')
except ValueError:
    print(f'invalid number: {user_data}')
except ZeroDivisionError:
    print(f'zero has no inverse')
