# Target Stock Prices - Line Chart
import pandas as pd
import matplotlib.pyplot as plt
import quandl

tgt = quandl.get('WIKI/TGT')
print(tgt)

plt.title('Target (TGT) closing stock prices', fontsize=20)
plt.xlabel('Year')
plt.ylabel('Stock price (USD)')
plt.plot(tgt.index, tgt['Adj. Close'])
plt.show()