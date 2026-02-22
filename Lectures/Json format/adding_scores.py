

import json
from readingScores import read_scores

filename = input('File name: ')

try:
    with open(filename, 'r') as f:
        grade_book = json.load(f)
except FileNotFoundError:
    grade_book = dict()

readingScores.read_scores(grade_book)

with open(filename, 'w') as f:
    json.dump(grade_book, f)

