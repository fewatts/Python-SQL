import pandas as pd

df = pd.DataFrame({'A': ['1', '2', '3', '4']})
df['A'] = df['A'].astype(int)
print(df)
