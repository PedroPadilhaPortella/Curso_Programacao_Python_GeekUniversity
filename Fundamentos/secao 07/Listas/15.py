from random import randint

lista = []
for i in range(0, 20):
    lista.append(randint(1, 10))

lista2 = []
for i in lista:
    if(i not in lista2):
        lista2.append(i)
lista2.sort()

conjunto = set(lista)
print(lista)
print(lista2)
print(conjunto)