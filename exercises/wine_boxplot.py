# Wine Dataset - Boxplot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

wine = load_wine()
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)

subset = wine_df[['malic_acid', 'ash', 'total_phenols', 'flavanoids',
                  'proanthocyanins', 'od280/od315_of_diluted_wines']]

ax = sns.boxplot(x="variable", y="value", fliersize=0., data=pd.melt(subset))
ax.set_xticklabels(['ma', 'ash', 'phe', 'fla', 'pro', 'od'])
plt.show()