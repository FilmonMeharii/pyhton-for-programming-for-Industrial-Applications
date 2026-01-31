number = int(input('Enter a number of socks: '))
print(f'Number of socks in the washing machine is : {number:.0f}')
pairs = number//2
amount = number % 2
print(f'There are {pairs:.0f} pairs and {amount:.0f} leftover sock')

left = int(input('Number of left shoes: '))
right = int(input('Number of right shoes: '))
pairs = min(left, right)
leftover = max(right, left)- pairs
print(f'There are {pairs:.0f} pairs and {leftover:.0f} leftover shoe(s)')