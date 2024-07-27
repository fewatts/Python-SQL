import pandas as pd

df = pd.DataFrame({'A': [1, 2, None, 4],
                   'B': [4, None, 2, 1]})
df_filled = df.fillna(0)
print(df_filled)
