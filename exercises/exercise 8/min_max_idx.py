# Finding Min and Max Indices
import pandas as pd

# Load data
url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv'
titanic_df = pd.read_csv(url)

# Find youngest and oldest passengers
youngest_idx = titanic_df['Age'].idxmin()
oldest_idx = titanic_df['Age'].idxmax()
youngest_oldest_df = titanic_df.iloc[[youngest_idx, oldest_idx]]
print("Youngest and oldest passengers:")
print(youngest_oldest_df[['Name', 'Age']])
print()

# Find lowest paying survivor and highest paying non-survivor
survivors_df = titanic_df[titanic_df['Survived'] == 1]
lowest_paying_survivor_idx = survivors_df['Fare'].idxmin()

non_survivors_df = titanic_df[titanic_df['Survived'] == 0]
highest_paying_non_survivor_idx = non_survivors_df['Fare'].idxmax()

highest_lowest_df = titanic_df.loc[[lowest_paying_survivor_idx, highest_paying_non_survivor_idx], 
                                    ['Name', 'Fare', 'Survived']]
print("Lowest paying survivor and highest paying non-survivor:")
print(highest_lowest_df)