

class Person:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
class Account:
    def __init__(self):
        self.holder = Person()
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount


    
checking = Account()
checking.balance = 1000
savings = checking
savings.balance = 500

import copy
checking = Account()    
checking.balance = 1000
savings = copy.copy(checking)
savings.balance = 500


checking = Account()
checking.balance = 500
checking.holder.first_name = 'John'
checking.holder.last_name = 'Doe'
print(f"Checking account holder: {checking.holder.first_name} {checking.holder.last_name}, balance: {checking.balance}")


import copy
savings = copy.copy(checking)
savings.balance = 400
savings.holder.first_name = 'Jane'