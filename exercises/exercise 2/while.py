

t = 10
while t >= 0:
  print(t)
  t -=1
print('Happy New Year!')

R = 2000
months = 0
while R < 20000:
  R += 0.1 * R * ( 1-R/ 25000)
  months += 1
print(months)