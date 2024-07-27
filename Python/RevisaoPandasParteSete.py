import pandas as pd

df = pd.DataFrame({'A': ['foo', 'foo', 'bar', 'bar'],
                   'B': ['one', 'two', 'one', 'two'],
                   'C': [1, 2, 3, 4]})

pivot_table = df.pivot_table(values='C', index='A', columns='B', aggfunc='sum')

print(pivot_table)
