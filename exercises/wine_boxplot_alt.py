# Wine Dataset - Alternative Boxplot
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine = load_wine()
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)

subset = wine_df[['malic_acid', 'ash', 'total_phenols', 'flavanoids',
                  'proanthocyanins', 'od280/od315_of_diluted_wines']]

ax = subset.boxplot(column=['malic_acid', 'ash', 'total_phenols', 'flavanoids',
                            'proanthocyanins', 'od280/od315_of_diluted_wines'], 
                    grid=False, vert=False)
ax.set_yticklabels(['ma', 'ash', 'phe', 'fla', 'pro', 'od'])
plt.show()