
def is_pangram(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in text.lower():
            return False
    return True

text = 'The quick brown fox jumps over the lazy dog.'
if is_pangram(text):
    print('The text is a pangram.')      # This will be printed
else:
    print('The text is not a pangram.')


text = 'This is just any text.'
if is_pangram(text):
    print('The text is a pangram.')
else:
    print('The text is not a pangram.')   # This will be printed