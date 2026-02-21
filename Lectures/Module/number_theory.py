import math


def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
