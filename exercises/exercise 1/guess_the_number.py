
import random

secret_number = random.randint(1, 20)
count_guesses = 0
for i in range(1, 20):
    guess = int(input('Enter your guess: '))            
    count_guesses += 1
    if guess < secret_number:        
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        print('Congratulations! You guessed the number!')
        break
print(f'You made {count_guesses} guesses.')