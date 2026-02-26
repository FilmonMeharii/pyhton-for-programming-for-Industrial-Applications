


def filter_dct(dct, threshold):
    new_dct = {}
    for key in dct:
        if dct[key] > threshold:
            new_dct[key] = dct[key]
    return new_dct
d = {'Nisse': 43, 'Birger': 21, 'MÅG': 35, 'Frida': 12, 'Folk': 20}
the_elite = filter_dct(d, 30)
print(the_elite)               # {'Nisse': 43, 'MÅG': 35}