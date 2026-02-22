

import json


en_fr = {'one': 'un', 'two': 'deux', 'three': 'trois'}
with open('en_fr.json', 'w') as f:
    json.dump(en_fr, f)

with open('en_fr.json', 'r') as f:
    translation = json.load(f)