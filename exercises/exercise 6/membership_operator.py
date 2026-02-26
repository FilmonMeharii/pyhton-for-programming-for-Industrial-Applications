


def robbers_language(word):
    vowels = frozenset('aeiouAEIOU')
    translation = ''

    for char in word:
        translation += char
        if char in vowels:
            translation += 'b' + char   
    return translation

english_word = input("Write a word: ")
translated_word = robbers_language(english_word)
print(f"Robber's language: {translated_word}")
    