# Inspecting DataFrames
import pandas as pd

# Load data
url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv'
titanic_df = pd.read_csv(url)

# Check if empty
if titanic_df.empty:
    print('Empty')
else:
    print('Not empty')
print()

# Create empty DataFrame and check
empty_df = pd.DataFrame()
if empty_df.empty:
    print('Empty DataFrame is empty')
else:
    print('Empty DataFrame is not empty')
print()

# Shape and size
print(f"Shape: {titanic_df.shape}")  # (rows, columns)
print(f"Size: {titanic_df.size}")    # total values
print()

# Data types
print("Data types:")
print(titanic_df.dtypes)
print()

# Column info
print("Column info:")
titanic_df.info()
print()

# Statistical summary
print("Statistical summary:")
print(titanic_df.describe())