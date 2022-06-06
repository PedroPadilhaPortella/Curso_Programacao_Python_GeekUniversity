'''
Generators

    Generators são Iterators.
    Geradores são funções que retornam um valor e são utilizados para gerar valores infinitos.
    Funções Geradores usam a palavra reservada yield.
    Generators podem ser criados com Funções Geradoras ou com a palavra reservada Generator Expression.
'''

#  Uma Generator Function
def count_until(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

#  Uma Generator Function gera um Generator
contar = count_until(10)

print(next(contar))

for n in contar:
    print(n)
