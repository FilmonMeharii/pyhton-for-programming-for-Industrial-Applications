import random

rolls = 0

while True:
    roll = random.randint(1, 6)
    rolls += 1
    print(f'You rolled a {roll}')
    if roll == 6:
        print(f'It took you {rolls} rolls to get a 6.')
        break