import pandas as pd

# tranformando dataframes com função pivot nela é possível determinar o que será index, colunas e quais serão os valores das mesmas
df = pd.DataFrame({'A': ['foo', 'foo', 'bar', 'bar'],
                   'B': ['one', 'two', 'one', 'two'],
                   'C': [1, 2, 3, 4]})

pivoted = df.pivot(index='A', columns='B', values='C')

print(pivoted)
