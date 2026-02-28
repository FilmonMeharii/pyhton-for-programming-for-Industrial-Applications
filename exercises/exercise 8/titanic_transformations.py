# Transformations on Titanic Dataset
import pandas as pd

# Load data
url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv'
titanic_df = pd.read_csv(url)

# Robust scaling for Fare (using IQR)
q3 = titanic_df['Fare'].quantile(.75)
q1 = titanic_df['Fare'].quantile(.25)
iqr = q3 - q1
median = titanic_df['Fare'].median()
titanic_df['Fare_robust'] = (titanic_df['Fare'] - median) / iqr

print("Original Fare stats:")
print(titanic_df['Fare'].describe())
print()
print("Robust scaled Fare stats:")
print(titanic_df['Fare_robust'].describe())