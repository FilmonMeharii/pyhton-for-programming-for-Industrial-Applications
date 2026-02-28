# Titanic Fares by Deck - Boxplot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv'
titanic_df = pd.read_csv(url)

titanic_df['Deck'] = titanic_df['Cabin'].str[0]

ax = sns.boxplot(x="Deck", y="Fare", order=['A', 'B', 'C', 'D', 'E', 'F', 'G'], 
                 fliersize=0., data=titanic_df)
ax.set(ylim=(0, 280))
plt.show()