# Titanic Passengers by Class - Bar Chart
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv'
titanic_df = pd.read_csv(url)

sns.set(style="whitegrid", color_codes=True)
plt.title('Titanic passengers by class', fontsize=20)
sns.countplot(x='Pclass', color='b', data=titanic_df)
plt.show()