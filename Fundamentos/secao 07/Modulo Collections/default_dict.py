'''
Module Collections -> High Performance Container Datetypes

Default Dict (Valor Padrão de Dicionários) => Ao criar um dicionário com Default Dict, recebe um valor padrão desse dicionário, evitando que hajam KeyErrors no seu projeto quando é buscado o valor de uma chave que não foi definida, usando lambda expressions.
'''

from collections import defaultdict

dicionario = defaultdict(lambda: "Valor não definido")
dicionario['nome'] = 'pedro'
dicionario['idade'] = 19

print(dicionario)
print(dicionario['nome'])
print(dicionario['nulo']) # esse campo não existe, e por isso chama o valor padrão
print(dicionario)

help(defaultdict)