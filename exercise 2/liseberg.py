

print('Welcome to Radiobilarna!')
height = int(input('How tall are you? '))
if height >= 130:
  print('You can go')
  print('Enjoy the ride!')
else:   
  print('Sorry, you aren\'t enough tall to ride.')            


print('Welcome to Lisebergbanan!')
height = int(input('How tall are you? '))
if height >= 130:
  print('You can go')
elif height >= 110:
  print('You may go if accompanied by an adult')
else: 
  print('Not tall enough')
  print('You cannot go')