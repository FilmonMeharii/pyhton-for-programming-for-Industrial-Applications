

import pandas as pd


ages = [23, 25, 21, 25]
students = ['Adam', 'Bobby', 'Celia', 'Daisy']
series = pd.Series(ages, index=students)
print(series)

ages = [23, 25, 21, 25]
students = ['Adam', 'Bobby', 'Celia', 'Daisy']
series = pd.Series(ages, index=students, name='Ages')
print('Series with names as index:')
print(series)
print()

student_ages = {'Adam': 23, 'Bobby': 25, 'Celia': 21, 'Daisy': 25}
series = pd.Series(student_ages, name='age', dtype='int')
print('Series from dictionary:')
print(series)
print()

same_age = 25
students = ['Adam', 'Bobby', 'Celia', 'Daisy']
series = pd.Series(same_age, index=students)
print('Series from scalar (all 25):')
print(series)