

import number_theory

x = int(input("Enter a number: "))
if number_theory.is_prime(x):
    print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")