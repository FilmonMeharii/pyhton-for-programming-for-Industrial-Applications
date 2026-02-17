

s = 'connexion'
print(f'There is an x in {s}: {"x" in s}')


print('old' in 'folded')

s ='Some sensetive subject'
for c in s:
    if c in 'aeiouy':
        print(c, end=' ')
    else:
        print(c, end='')
        