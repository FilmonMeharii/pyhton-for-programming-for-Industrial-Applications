# Titanic Fares by Deck - Stripplot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv'
titanic_df = pd.read_csv(url)

titanic_df['Deck'] = titanic_df['Cabin'].str[0]

plt.title('Fares paid by passengers of the Titanic by deck', fontsize=20)
sns.stripplot(x="Deck", y="Fare", order=['A', 'B', 'C', 'D', 'E', 'F', 'G'], 
              jitter=False, data=titanic_df)
plt.show()