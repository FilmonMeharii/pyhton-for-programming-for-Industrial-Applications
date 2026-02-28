# Titanic Passengers by Class - Pie Chart
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv'
titanic_df = pd.read_csv(url)

a = titanic_df[titanic_df.Pclass == 1]["Pclass"].count()
b = titanic_df[titanic_df.Pclass == 2]["Pclass"].count()
c = titanic_df[titanic_df.Pclass == 3]["Pclass"].count()

labels = 'First', 'Second', 'Third'
sizes = [a, b, c]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Titanic passengers by class', fontsize=20)

patches, texts = plt.pie(sizes)
plt.legend(patches, labels, loc="lower right")
plt.axis('equal')
plt.show()