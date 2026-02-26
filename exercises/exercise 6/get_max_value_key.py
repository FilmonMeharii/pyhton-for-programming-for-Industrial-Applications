

def get_max_value_key(d):
    max_key = None
    max_value = float('-inf')
    
    for key, value in d.items():
        if value > max_value:
            max_value = value
            max_key = key
            
    return max_key

d = {'Nisse': 43, 'Birger': 21, 'MÅG': 35, 'Frida': 12, 'Folk': 20}
winner = get_max_value_key(d)
print(f'The winner is {winner} with {d[winner]} votes.')  # Nisse, 43