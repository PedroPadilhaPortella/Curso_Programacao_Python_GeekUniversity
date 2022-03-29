'''
Listas Aninhadas ( Nested Lists )

Algumas linguagens de programação possuem uma estrutura de dados chamados de arrays,
que podem ser unidimensionais ou multidimensionais, como C, Java, PHP.
Em Pyhton as listas podem ser unidimensionais ou multidimensionais.
'''
from random import choice

matriz = [[1, 2, 3], [4, 5, 6],  [7, 8, 9]]

for l in range(0, len(matriz)):
    for c in range(0, len(matriz[l])):
        print(f"[{matriz[l][c]}]", end=' ')
    print()
print()

for lista in matriz:
    for numero in lista:
        print(f"[{numero}]", end=' ')
    print()

# List Comprehension

[[print(f'[{valor}]', end=' ') for valor in lista] for lista in matriz]

# Gerando um tabuleiro

tabuleiro = [[numero for numero in range(1, 5)] for valor in range(1, 5)]
print(f"\n\n{tabuleiro}")
print()

# Gerando jogo da velha


velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
for lista in velha:
    for numero in lista:
        print(f"[{numero}]", end=' ')
    print()
print()

# Gerando jogo da velha aleatório
    
velha = [[choice(['X', 'O']) for numero in range(3)] for valor in range(3)]

for lista in velha:
    for numero in lista:
        print(f"[{numero}]", end=' ')
    print()

# Gerando valores iniciais
print([[0 for i in range(4)] for j in range(4)]) 
print([['-' for i in range(4)] for j in range(4)]) 