

i = 0
total = 0
while i < 10:
    offer = int(input('What is your offer? '))
    if offer < 150:
        print(f'I\'m not selling for that price!')
        continue
    total += offer
    i += 1
print(f'Total sales revenue: {total} ')
