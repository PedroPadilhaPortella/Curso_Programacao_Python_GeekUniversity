'''
Zip
    zip() -> Cria um iterável (Zip Object) que agrega os elementos de cada um
    dos iteráveis passados como entrada em pares.
'''

lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
lista3 = [1, 2]

print(list(zip(lista1, lista2)))
print(tuple(zip(lista1, lista2)))
print(set(zip(lista1, lista2)))
print(dict(zip(lista1, lista2)))

# O zip utiliza como parametro, o menor iteravel, no caso de iteraveis com tamanhos diferentes.
print(list(zip(lista1, lista2, lista3)))

# Podemos usar diferentes tipos de iteráveis no zip
tupla = 1, 2, 3 
set = set(['pedro', 'daniel', 'samuel']) 
print(dict(zip(set, tupla)))


dados = [(1,2), (1,2), (1,2), (1,2)]
print(tuple(zip(*dados)))


# Exemplo -> a nota final sera a  maior nota
p1 = [90, 88, 94]
p2 = [98, 77, 87]
alunos = ['portella', 'casalli', 'bunhak']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, p1, p2)}
print(final)