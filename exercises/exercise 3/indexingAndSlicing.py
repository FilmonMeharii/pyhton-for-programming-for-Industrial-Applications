
word = input('Write a word: ')
first = word[0]        # first character of the string
fourth =  word[3]       # fourth character of the string
last =    word[-1]       # last character: remember that we do not know the length of the string!
reverse = word[::-1]      # use slicing to reverse the string
print(f'The word starts with {first} and ends with {last}.')
print(f'The fourth character is {fourth}.')
print(f'The reverse is {reverse}.')