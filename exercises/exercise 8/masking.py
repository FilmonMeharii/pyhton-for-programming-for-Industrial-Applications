# Selecting Columns
import pandas as pd

# Load data
url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv'
titanic_df = pd.read_csv(url)

# Select single column (returns Series)
survived_series = titanic_df['Survived']
print("Single column (Series):")
print(survived_series.head())
print()

# Select multiple columns (returns DataFrame)
cols = ['Sex', 'Survived']
survived_sex_df = titanic_df[cols]
print("Multiple columns (DataFrame):")
print(survived_sex_df.head())
print()

# Find numerical columns
print("Numerical columns:")
for col in titanic_df.columns:
    series = titanic_df[col]
    if series.dtype in ['int64', 'float64']:
        print(f"{col}: {series.dtype}")