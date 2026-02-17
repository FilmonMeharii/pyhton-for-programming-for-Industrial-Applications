

text = 'This is my sample text'

for letter in text:
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vouls = 'aeiouAEIOU'
    if letter in consonants:
        print(letter +'o'+ letter, end='')
    else:
        print(letter, end='')
print()
print(text)