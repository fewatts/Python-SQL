import pandas as pd

# 1º Criando dataframes (Que são coleções de dados bidirecionais)
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}

df = pd.DataFrame(data)

print(df)

# 2º Adicionando colunas
df['Age in 10 Years'] = df['Age'] + 10

print(df)
