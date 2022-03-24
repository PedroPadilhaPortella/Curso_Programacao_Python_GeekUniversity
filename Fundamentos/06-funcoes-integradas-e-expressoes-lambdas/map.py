'''
Map
    Com o map, fazemos mapeamento de valores para funções.
    Ela é uma função que recebe dois paramentros, uma função e um iterável,
    que pode ser uma lista, tupla, etc... e retorna um <map object>, que é
    Map Object: f(a), f(b), f(c), f(d) ... sendo f() a função passada por parâmetro.
'''

import math


def area(raio):
    return math.pi * math.pow(raio, 2)

values = [1, 2, 3, 4, 5, 6, 7, 8]

# areas = []
# for r in raios:
#     areas.append(area(r))
areas = map(area, values)

print(list(areas))
print(type(areas))

# Map com Lambda
print(list(map(lambda  r: math.pi * math.pow(r, 2), values)))


cidades = [('Berlim', 29), ('Cairo', 32), ('Buenos Aires', -3), ('São Paulo', 19), ('NY', 23)]
celcius_to_fahrenheit = lambda item: (item[0], 9/5 * item[1] + 32)

print(cidades)

print(list(map(celcius_to_fahrenheit, cidades)))