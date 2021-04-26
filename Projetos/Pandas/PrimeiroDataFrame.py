import pandas as pd


data = {
    'Alunos': ['pedro', 'joao', 'vinicius', 'gabriel', 'linda', 'dieffany', 'tamilys', 'damares', 'agnes'],
    'Idades': [19, 20, 20, 19, 20, 20, 19, 20, 19],
    'Notas': [10, 9, 10, 8, 7, 6, 4, 6, 6]
}

df = pd.DataFrame(data, columns=['Alunos', 'Idades', 'Notas'])


df.describe()

df = df.drop([0, 1])

#df = df.drop('Idades', axis=1)

df.count()

df.columns

df.shape


df.max()

df['Notas'].max()

df.min()

df['Notas'].min()

df.mean()

df.median()

df.sum()


df['Idades'].add(10)

df['Notas'].sub(1)

df['Notas'].mul(10)

df['Notas'].div(2)

df['Notas'][1]


df.head()

df.tail()

df.loc[df['Notas'] >= 8]

df.loc(df['Notas'] == 10)