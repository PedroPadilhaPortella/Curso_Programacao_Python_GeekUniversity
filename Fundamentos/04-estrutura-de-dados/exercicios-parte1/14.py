# from collections import defaultdict
# from random import randint

# lista = []
# for i in range(0, 10):
#     lista.append(randint(1, 10))
# keys = defaultdict(list)
# print(lista)

# for key, value in enumerate(lista):
#     keys[value].append(key)

# for value in keys:
#     if len(keys[value]) > 1:
#         print(value, keys[value])

from random import randint

lista = []
for i in range(0, 10):
    lista.append(randint(1, 10))
print(lista)

listaTeste = []
for i in lista:
    if(i in listaTeste):
        continue
    print("Repeticoes de {}: {}".format(i, lista.count(i)))
    listaTeste.append(i)