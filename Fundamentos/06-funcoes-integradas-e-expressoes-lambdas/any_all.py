'''
Any
    Função Booleana que retorna true se algum dos elementos do iterável são verdadeiros para uma condição.
All
    Função Booleana que retorna true se todos os elementos do iterável são verdadeiros para uma condição,
    ou se o iterável é vazio.

'''
#All
print(all([1, 2, 3])) # Todos os elementos são verdadeiros? True
print(all([0, 1, 2, 3])) # Todos os elementos são verdadeiros? False
print(all([])) # Todos os elementos são verdadeiros? True
print(all({1, 2, 3})) # Todos os elementos são verdadeiros? False
print(all('iteravel de caracteres')) # Todos os elementos são verdadeiros? True

nomes = ['Carlos', 'Caique', 'Cintia', 'Ceronni']
print(nomes)
print("Todos os nomes comecam com C? ", all(nome[0] == 'C' for nome in nomes))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))


#Any
print(any([1, 2, 3, 4, 5])) # Algum dos elementos é verdadeiro? True
print(any([False, {}, [], (), ''])) # Algum dos elementos é verdadeiro? False

nomes = ['Carlos', 'Caique', 'Cintia', 'Daniel', 'Pedro']
print(nomes)
print("Algum dos nomes comeca com P? ", any(nome[0] == 'P' for nome in nomes))