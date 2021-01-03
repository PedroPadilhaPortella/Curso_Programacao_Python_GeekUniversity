'''
List Comprehention

- Utilizamos list comprehention, podemos gerar  listas com os dados processados a partir de outro iterável

- Sintaxe
[ dado for dado in iteravel ]
'''

import math

#Exemplos
numeros = [1, 2, 3, 4, 5]

resultados = [numero * 10 for numero in numeros]

print(resultados)

resultados = [resultado / 2 for resultado in resultados]

print(resultados)

# List omprehention com uma função

def funcao(i):
    return math.pow(i, 2)

resultados = [funcao(numero) for numero in numeros]

print(resultados)

'''
A vantagem do list comprehention é executar operações com listas usando for em uma única linha
'''

# 1
nome = "Pedro Portella"
print([letra.upper() for letra in nome])

# 2
amigos = ['casalli', 'vinicius', 'bunhak', 'pedro']
print([amigo.title() for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14, {}]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])

'''
Podemos adiciona estruturas lógicas dentro das list comprehensions
[dado for dado in dados if condicao]
'''

# 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares, impares)

# 2

res = [numero * 2 if numero % 2 else numero / 2 for numero in numeros]
print(res)