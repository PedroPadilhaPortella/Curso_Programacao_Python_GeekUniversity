tupla = (1, 2, 4)
lista = list(tupla)
lista.append(12)
print(tuple(lista))

tupla = tuple(range(0, 100, 5))
print(tupla)

tupla = 'Pedro portella da cruz', 19
nome, idade = tupla
print(idade, nome)

tupla = 9.2, 5.7, 10, 9.7, 6, 10
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

print(9.9 in tupla)
print(tupla.count(10))