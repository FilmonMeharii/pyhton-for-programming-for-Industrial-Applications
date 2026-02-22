
zahlen=['eins', 'zwei', 'drei']
german = dict(zip(zahlen, range(1,4)))
print(german)

s = {x**2 for x in range(4)}
p = {x: x**2 for x in range(4)}
print(s, p)