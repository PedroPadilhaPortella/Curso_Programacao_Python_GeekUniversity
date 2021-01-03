'''
Dictionary Comprehention

- Podemos criar dicionarios de forma compacta

- Sintaxe
{chave: valor for valor in iteravel condicao}
'''
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dicio = {chave:valor ** 2 for chave, valor in numeros.items()}

print(dicio)

# 1 

numeros = {1, 2, 3, 4, 5}
dicio = {valor - 1: (valor -1 )** 2 for valor in numeros}
print(dicio)

# 2
chaves = 'abcde'
valores = [7, 3, 24, 46, 3]
mix = {chaves[i]: valores[i] for i in range(0, len(valores))}
print(mix)

# com condicional

numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)