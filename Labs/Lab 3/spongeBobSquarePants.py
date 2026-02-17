


word = input('Write a word: ')
new_word = ''
for i in range(len(word)):
    if i % 2 == 0:
        new_word += word[i].lower()
    else:
         new_word += word[i].upper()    
print(new_word)