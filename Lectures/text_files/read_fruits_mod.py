


import os

here = os.path.dirname(__file__)
path = os.path.join(here, "fruits.txt")

with open(path, "r") as f:
    for line in f:
        print(line.strip())