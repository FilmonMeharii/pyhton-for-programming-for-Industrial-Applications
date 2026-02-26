

def scrabble(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    scores = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 1, 4, 4, 8, 4, 10]
    letter_scores = dict(zip(alphabet, scores))
    total = 0
    for char in word:
        total += letter_scores.get(char.lower(), 0)     
    return total

user_word = input("Write a word: ")
word_score = scrabble(user_word)
print(f"Scrabble score: {word_score}")