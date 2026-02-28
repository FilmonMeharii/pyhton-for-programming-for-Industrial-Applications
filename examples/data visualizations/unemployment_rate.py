# US Unemployment Rate - Line Chart
import pandas as pd
import matplotlib.pyplot as plt

unemployment = pd.read_csv('http://data-analytics.zybooks.com/unemployment.csv')

plt.title('U.S. unemployment rate', fontsize=20)
plt.xlabel('Year')
plt.ylabel('% of total labor force')
plt.plot(unemployment["Year"], unemployment["Value"])
plt.show()