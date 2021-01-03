'''
Set Comprehension

list = [1, 2, 3]
set = (1, 2, 3)
'''

numeros = {num for num in range(7)}
print(numeros)

numeros = {x ** 2 for x in range(10)}
print(numeros)


letras = {letra for letra in 'kaiak'}
print(letras)