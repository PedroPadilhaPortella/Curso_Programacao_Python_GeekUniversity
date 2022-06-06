'''
Entendendo Iterators e Iterables

    Iterators -> são objetos que podem ser iterados.
    Um objeto que retorna um valor a cada chamada de um método next()

    Iterables -> são objetos que podem ser convertidos em iterators.
    Um objeto que retorna um valor a cada chamada de um método iter()
'''

numeros = [1, 2, 3, 4, 5]

iter1 = iter(numeros)

for i in iter1:
    print(i)