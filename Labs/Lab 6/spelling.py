


import json


with open("phonetic_alphabet.json", "r") as file:
    alphabet = json.load(file)

word = input("Enter a word: ")

result = []
for letter in word:
    lower_letter = letter.lower()
code_word = alphabet.get(lower_letter, letter)
result.append(code_word)
print("Phonetic alphabet code:", " ".join(result))
