
# DataFrame Creation Examples
import pandas as pd

# DataFrame from nested list
students_ages = [['Adam', 23], ['Bobby', 25], ['Celia', 21], ['Daisy', 25]]
df = pd.DataFrame(students_ages, columns=['Name', 'Age'])
print("DataFrame from nested list:")
print(df)
print()

# DataFrame from dict of lists
students = ['Adam', 'Bobby', 'Celia', 'Daisy']
ages = [23, 25, 21, 25]
students_ages = {'Name': students, 'Age': ages}
df = pd.DataFrame(students_ages)
print("DataFrame from dict of lists:")
print(df)
print()

# DataFrame from dict of Series
students = ['Adam', 'Bobby', 'Celia', 'Daisy']
ages = [23, 25, 21, 25]
names_series = pd.Series(students, name='Name')
ages_series = pd.Series(ages, name='Age')
students_ages = {'Name': names_series, 'Age': ages_series}
df = pd.DataFrame(students_ages)
print("DataFrame from dict of Series:")
print(df)