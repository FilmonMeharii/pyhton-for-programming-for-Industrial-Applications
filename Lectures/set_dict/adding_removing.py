

m = {2,4,6}
m.add(8)
m.add(6)

m.discard(4)
m.remove(2)
m.discard(7)
#m.remove(7)

x = m.pop()
m.clear()

print(f'm = {m}')

en = {'one', 'two', 'three'}
for number in en:
    print(number, end=' '   )