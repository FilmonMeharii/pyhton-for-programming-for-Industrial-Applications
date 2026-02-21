

one_child_allowance = 1250
child = int(input("Enter number of children: "))

if child == 1:
    one_child_allowance = one_child_allowance + 0
elif child == 2:
    one_child_allowance = one_child_allowance + 150
elif child == 3:
    one_child_allowance = one_child_allowance + 730
elif child == 4:
    one_child_allowance = one_child_allowance + 1740
elif child > 5:
    one_child_allowance = one_child_allowance + 2990
elif child >= 6:
    one_child_allowance = one_child_allowance + 4240
print(f'The child allowance is : {one_child_allowance} ')


#case solution

child = int(input("Enter number of children: "))
one_child_allowance = 1250

match child:
    case 1:
        one_child_allowance += 0
    case 2:
        one_child_allowance += 150
    case 3:
        one_child_allowance += 730
    case 4: 
        one_child_allowance += 1740
    case 5:       
        one_child_allowance += 2990
    case _:
        one_child_allowance += 4240
print(f'The child allowance is : {one_child_allowance} ')   