import pandas as pd

# Realizando merge -> Combinando dataframes usando um parametro
df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                    'A': ['A0', 'A1', 'A2']})

df2 = pd.DataFrame({'key': ['K0', 'K1', 'K3'],
                    'B': ['B0', 'B1', 'B3']})

result = pd.merge(df1, df2, on='key')

print(result)
