# Handling Missing Data
import pandas as pd

# Load data
url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv'
titanic_df = pd.read_csv(url)

# Find rows with missing age
missing_age_df = titanic_df[titanic_df['Age'].isnull()]
print(f"Rows with missing age: {len(missing_age_df)}")
print(missing_age_df[['Name', 'Age']].head())
print()

# Find rows with any missing data (Age, Cabin, or Embarked)
missing_data_df = titanic_df[
    titanic_df['Age'].isnull() | 
    titanic_df['Cabin'].isnull() | 
    titanic_df['Embarked'].isnull()
]
print(f"Rows with any missing data: {len(missing_data_df)}")
print(missing_data_df[['Name', 'Age', 'Cabin', 'Embarked']].head())