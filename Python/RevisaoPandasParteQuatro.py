import pandas as pd

#Agrupando dataframes pela categoria e realizando a soma
df = pd.DataFrame({'Category': ['A', 'A', 'B', 'B'],
                   'Values': [1, 2, 3, 4]})

grouped = df.groupby('Category').sum()

print(grouped)
