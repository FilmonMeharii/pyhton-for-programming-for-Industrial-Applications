

from operator import neg
from turtle import pos


def sum_separately(*values):
    pos, neg = 0, 0
    for item in values:
        if item < 0:
            neg += item
        else:
            pos += item
    return pos, neg
        
revenue, expenses = sum_separately(2, 3, -2, -7, 0, 1)
print(f'Revenue: {revenue}, Expenses: {-expenses}')