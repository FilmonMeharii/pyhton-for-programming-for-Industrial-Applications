

def sum_first(n):
    res = 0
    for i in range(n):
        res += i
    return res

rate = 0.05
def compute_balance(amount, years):
    return amount * (1 + rate) ** years


def flip(lst):
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n - 1 - i] = lst[n - 1 - i], lst[i]
L = [1, 2, 3, 4, 5]
flip(L)
print(L)