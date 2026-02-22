


#sets and dictionaries are two built in types in python that stores objects

#set stores an unordered collection of unique elements
#dict stores a collection of key value pairs with unique keys

en = {'one', 'two', 'three'}
fr = {'un':1, 'deux':2, 'trois':3}

zahlen = ['eins', 'zwei', 'drei']
de= set(zahlen)
numeri = [('uno', 1), ('due', 2), ('tre', 3)]
it = dict(numeri)

es = dict(uno=1, due=2, tre=3)
print(en, fr, de, it, es)

empty = {}
void = dict()
nothing = set()


print(empty, void, nothing)


print(en) # {’two’, ’one’, ’three’}
print(fr) # {’un’: 1, ’deux’: 2, ’trois’: 3}
print(de) # {’zwei’, ’drei’, ’eins’}
print(it) # {’uno’: 1, ’due’: 2, ’tre’: 3}
print(es) # {’uno’: 1, ’dos’: 2, ’tres’: 3}
print(empty) # {}
print(void) # {}
print(nothing) # set()