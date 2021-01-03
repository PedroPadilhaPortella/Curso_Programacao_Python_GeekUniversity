'''
Module Collections -> High Performance Container Datetypes

Ordered Dict () => Os dicionários não possuem uma ordem definida, usando o OrderedDict, a ordem das chaves se torna imutável, de modo que tras segurança para aplicações que precisem disso.
'''

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'c': 7, 'e': 2, 'b': 33, 'd': 0 })

print(type(dicionario))
print(dicionario)

for k, v in dicionario.items():
    print(f"{k}: {v}")

d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}

print(d1 == d2) # a ordem não faz diferenca

d3 = OrderedDict({'a': 1, 'b': 2})
d4 = OrderedDict({'b': 2, 'a': 1})

print(d3 == d4) # a ordem faz diferenca