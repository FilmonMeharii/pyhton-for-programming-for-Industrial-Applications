import pandas as pd

df = pd.read_csv('used_vehicles_craigslist.csv', sep=';')

# Now group by state (column exists!)
avg_prices = df.groupby('state')['price'].mean().round().astype(int)

# Sort from highest to lowest and get top 10
top_10_states = avg_prices.sort_values(ascending=False).head(10)

# Print the Series
print(top_10_states)