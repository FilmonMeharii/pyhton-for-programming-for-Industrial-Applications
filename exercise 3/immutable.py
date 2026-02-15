

word = input('Write a word: ')
new_word = ''
for letter in word:
  if letter in {'a', 'e', 'i', 'o', 'u', 'y'}:
    new_word += letter.upper()
  else:
    new_word += letter.lower()
print(new_word)