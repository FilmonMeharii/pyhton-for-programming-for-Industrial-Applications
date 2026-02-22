

def pig_latin(word):
    if word[0] in 'aeiouy':
        return word + 'way'
    else:
        for i, letter in enumerate(word):
            if letter.lower() in 'aeiouy':
                return word[i:] + word[:i] + 'ay'
    return word
print(pig_latin('hello'))
print(pig_latin('apple'))