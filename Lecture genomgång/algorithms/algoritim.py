
n = int(input("Number: "))
is_prime = True
for k in range(2, n):
    if n % k == 0:
        is_prime = False
print('Prime: ', is_prime)


n = int(input("Number: "))
is_prime = True
for k in range(2, n):
    if n % k == 0:
        is_prime = False
        break
print('Prime: ', is_prime)