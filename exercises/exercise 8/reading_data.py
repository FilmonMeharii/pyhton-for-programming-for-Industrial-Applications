# Reading Data from Files
import pandas as pd

# Reading Titanic dataset from URL
url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv'
titanic_df = pd.read_csv(url)
print("Titanic dataset:")
print(titanic_df)
print()

# Reading wine dataset from scikit-learn
from sklearn.datasets import load_wine
wine = load_wine()
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
print("Wine dataset:")
print(wine_df)