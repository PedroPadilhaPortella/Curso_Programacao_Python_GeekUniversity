import pandas as pd

df = pd.read_csv('servicos.csv')

df.describe()

df.columns

df.count()

df = df.drop('Subclasse', axis=1)
