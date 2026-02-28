

#!pip install --upgrade quandl
# loads the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import quandl
import seaborn as sns
from sklearn.datasets import load_wine


url = 'https://datahub.io/core/natural-gas/r/daily.csv'
gas_prices_df = pd.read_csv(url)
ax = gas_prices_df.plot(x='Date', y='Price')
plt.xticks(rotation=90)
plt.title('Natural gas prices in dollars')
plt.show()

# loads the unemployment dataset
unemployment = pd.read_csv('http://data-analytics.zybooks.com/unemployment.csv')

# title
plt.title('U.S. unemployment rate', fontsize = 20)

# x and y axis labels
plt.xlabel('Year')
plt.ylabel('% of total labor force')

# plot
plt.plot(unemployment["Year"], unemployment["Value"])

# saves the image
#plt.savefig("linechart.png")

# shows the image
plt.show()


# creates a data frame containing TGT stock data
tgt = quandl.get('WIKI/TGT')
print(tgt)

# title
plt.title('Target (TGT) closing stock prices', fontsize=20)

# x and y axis labels
plt.xlabel('Year');
plt.ylabel('Stock price (USD)');

# plot
plt.plot(tgt.index, tgt['Adj. Close'])

# saves the image
#plt.savefig("tgtstocklinechart.png")

plt.show()


# loads the titanic dataset
url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv'
titanic_df = pd.read_csv(url)

# sets the style of the bar charts
sns.set(style="whitegrid", color_codes=True)

# title
plt.title('Titanic passengers by class', fontsize=20)

# plots a vertical bar chart
sns.countplot(x='Pclass', color='b', data=titanic_df);

# saves the image
#plt.savefig('verticalbarchart.png')

# shows the image
plt.show()


# sets the style of the bar charts
sns.set(style="whitegrid", color_codes=True)

# title
plt.title('Titanic survivors and deaths by class', fontsize=20)

# generates a vertical bar chart
sns.countplot(x="Pclass", hue="Survived", color="b", data=titanic_df);

# saves the image
#plt.savefig("groupedbarchart.png")

# shows the image
plt.show()

# counts the number of passengers for each class
a = titanic_df[titanic_df.Pclass == 1]["Pclass"].count()
b = titanic_df[titanic_df.Pclass == 2]["Pclass"].count()
c = titanic_df[titanic_df.Pclass == 3]["Pclass"].count()

# data to plot
labels = 'First', 'Second', 'Third'
sizes = [a, b, c]

# plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# title
plt.title('Titanic passengers by class', fontsize=20)

# legend
patches, texts = plt.pie(sizes)
plt.legend(patches, labels, loc="lower right")

# produces a perfectly circular chart
plt.axis('equal')

# saves the image
#plt.savefig("piechart.png")

# shows the image
plt.show()


# element-wise reading of the cabin number, interpreting the first character as the deck
titanic_df['Deck'] = titanic_df['Cabin'].str[0]

# title
plt.title('Fares paid by passengers of the Titanic by deck', fontsize=20)

# plot
sns.stripplot(x="Deck", y="Fare", order=['A', 'B', 'C', 'D', 'E', 'F', 'G'], jitter=False, data=titanic_df)

# saves the image
#plt.savefig("titanicstripplot.png")

# shows the image
plt.show()

ax = sns.boxplot(x="Deck", y="Fare", order=['A', 'B', 'C', 'D', 'E', 'F', 'G'], fliersize=0., data=titanic_df)
ax.set(ylim=(0, 280))
plt.show()

wine = load_wine()
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
subset = wine_df[['malic_acid', 'ash',
       'total_phenols', 'flavanoids',
       'proanthocyanins',
       'od280/od315_of_diluted_wines']]
ax = sns.boxplot(x="variable", y="value", fliersize=0., data=pd.melt(subset))
ax.set_xticklabels(['ma', 'ash', 'phe', 'fla', 'pro', 'od'])
plt.show()

ax = subset.boxplot(column = ['malic_acid', 'ash',
       'total_phenols', 'flavanoids',
       'proanthocyanins',
       'od280/od315_of_diluted_wines'], grid = False, vert=False);
ax.set_yticklabels(['ma', 'ash', 'phe', 'fla', 'pro', 'od'])
plt.show()