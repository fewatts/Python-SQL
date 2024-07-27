import pandas as pd

#Criando categorias para numeros e valores usando a função multi index
arrays = [['A', 'A', 'B', 'B'], ['one', 'two', 'one', 'two']]

index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'Number'))

df = pd.DataFrame({'Values': [1, 2, 3, 4]}, index=index)

print(df)
