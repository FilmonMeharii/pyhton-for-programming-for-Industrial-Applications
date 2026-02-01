

i = float(input('Enter the initial investment amount: '))
goal = float(input('Enter the goal amount: '))
interest_rate = 4.5
years = 0

while i < goal:
    i = i + (interest_rate/100)* i
    years += 1
print(f'After {years} years, the investment will reach at least {goal}. Final amount: ${i:.2f}')

