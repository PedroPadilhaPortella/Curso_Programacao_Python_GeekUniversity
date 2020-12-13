'''
Module Collections -> High Performance Container Datetypes

Named Tuple() => São tuplas que possuem propridades nomeadas, semelhantes a objetos ou dicionarios
'''

from collections import namedtuple

# Declaracao forma 1
cachorro = namedtuple('cachorro', 'idade raca nome')
# Declaracao forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')
# Declaracao forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Aplicacao
bob = cachorro(idade=2, raca='pitbull', nome='bob')

print(bob)
print(type(bob))

print(bob[0])
print(bob[1])
print(bob[2])
print(bob.idade)
print(bob.raca)
print(bob.nome)

