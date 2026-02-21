


#list are Mutable can changes 
#tuple are immutable can not change
s = 'Hello'
ls = list(s) # [’H’, ’e’, ’l’, ’l’, ’o’]
ts = tuple(ls)

lst = [456, 218, 101, 212] #square brackets
tpl = (11, 240, 244, 278) #parentheses

#they both can have zero eelements
empty_list = []
empty_tuple = ()

#tuples can be created without parentheses
tpl2 = 1, 2, 3, 4
tpl3 = 1, 2, 3, 4, #trailing comma is needed for single element tuple

#they both can have different data types
lst2 = [1, 'hello', 3.14, [1, 2, 3], (4, 5, 6)]
tpl4 = (1, 'hello', 3.14, [1, 2, 3], (4, 5, 6))

s = 'Hello'
lst3 = list(s) # [’H’, ’e’, ’l’, ’l’, ’o’]
tpl5 = tuple(s) # (’H’, ’e’, ’l’, ’l’, ’o’) 

print(lst3)
print(tpl5)

lst4 = [1, 2, 3]
tpl6 = (4, 5, 6)    

print(lst4[0]) # 1
print(tpl6[0]) # 4

#slicing
print(lst4[1:]) # [2, 3]        
print(tpl6[1:]) # (5, 6)

