import pandas as pd

vals = [[12, 13], [17, 14], [11, 15]]
cols = ['Spring', 'Fall']
idx = ['2020', '2021', '2022']
df = pd.DataFrame(vals, columns=cols, index=idx)
print(df)