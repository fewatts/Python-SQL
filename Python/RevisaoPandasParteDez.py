import pandas as pd

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar'],
                   'B': [1, 2, 1, 2]})
cleaned_df = df.drop_duplicates()
print(cleaned_df)
