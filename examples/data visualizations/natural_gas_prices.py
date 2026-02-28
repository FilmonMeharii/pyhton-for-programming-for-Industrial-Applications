# Natural Gas Prices - Line Chart
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://datahub.io/core/natural-gas/r/daily.csv'
gas_prices_df = pd.read_csv(url)
ax = gas_prices_df.plot(x='Date', y='Price')
plt.xticks(rotation=90)
plt.title('Natural gas prices in dollars')
plt.show()