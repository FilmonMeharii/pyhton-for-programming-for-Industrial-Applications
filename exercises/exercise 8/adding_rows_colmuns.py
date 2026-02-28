# Adding Rows and Columns
import pandas as pd
from sklearn.datasets import load_wine

# Load wine dataset
wine = load_wine()
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
print("Original wine dataset shape:", wine_df.shape)
print()

# Add a new row
nb_rows, nb_cols = wine_df.shape
new_row = pd.Series(0., index=wine_df.columns)
wine_df.loc[nb_rows] = new_row  # Add at the end
print("After adding a row, shape:", wine_df.shape)
print()

# Add a new column (standardized alcohol)
mu = wine_df['alcohol'].mean()
sigma = wine_df['alcohol'].std()
wine_df['alcohol_standardized'] = (wine_df['alcohol'] - mu) / sigma
print("Added standardized alcohol column:")
print(wine_df[['alcohol', 'alcohol_standardized']].head())
print()

# Robust scaling using IQR
q3 = wine_df['alcohol'].quantile(.75)
q1 = wine_df['alcohol'].quantile(.25)
iqr = q3 - q1
median = wine_df['alcohol'].median()
wine_df['alcohol_robust'] = (wine_df['alcohol'] - median) / iqr
print("Added robust scaled alcohol column:")
print(wine_df[['alcohol', 'alcohol_robust']].head())
print()

# Normalize a column (0 to 1)
x = wine_df['color_intensity']
x_min = x.min()
x_max = x.max()
wine_df['color_intensity_normalized'] = (x - x_min) / (x_max - x_min)
print("Normalized color intensity:")
print(wine_df[['color_intensity', 'color_intensity_normalized']].head())