'''
Módulos são outros arquivos em Python que podem ser adicionados ao seu projeto,
    para extender as funcionalidades ou utilizar classes nativas do Pyhton ou
    classes desenvolvida por outros programadores da comunidade.

Random Module -> Possui varias funções para a geração de números pseudoaleatórios.
'''

from random import random, randint, uniform, choice, choices, shuffle

# Gera um aleatório entre 0 e 1
print(random())

# Gera um aleatório inteiro entre n e m
print(randint(0, 10))

# Gera um aleatório entre n e m
print(uniform(0, 10))

# Retorna um elemento aleatório de um iterável
print(choice(('pedra', 'papel', 'tesoura')))

# Retorna um conjunto de elementos aleatório de um iterável
print(choices(['pedra', 'papel', 'tesoura']))

# Embaralha os elementos de um iterável
cartas = ['Q', 'J', 'K', 'A', '2', '3']
shuffle(cartas)
print(cartas)