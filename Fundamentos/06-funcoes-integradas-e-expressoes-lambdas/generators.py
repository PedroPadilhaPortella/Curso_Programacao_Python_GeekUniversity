'''
Generatos
    Também chamados de Tuple Comprehentions, muito semelhante a List Comprehention.

    Performaticamente, o Generator ocupa menos recursos em memória que o List Comprehention, 
    uma vez que ele só gera os dados em memória quando aplicado a uma expressão.

'''
from sys import getsizeof


nomes = ['Carlos', 'Caique', 'Cintia', 'Daniel', 'Pedro']


print('Generator')
generator = (nome[0] == 'P' for nome in nomes)

nomes_p = any(generator)

print("Tipo: ", type(generator))
print("Size: ", getsizeof(generator))
print(nomes_p)



print('\n\nList Comprehention')
list_comprehention = [nome[0] == 'P' for nome in nomes]

nomes_p = any(list_comprehention)

print("Tipo: ", type(list_comprehention))
print("Size: ", getsizeof(list_comprehention))
print(nomes_p)
