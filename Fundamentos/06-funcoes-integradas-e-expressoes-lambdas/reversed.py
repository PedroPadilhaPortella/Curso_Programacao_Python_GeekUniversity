'''
Reversed
    reversed() -> Serve para reverter os elementos de acordo com uma expressão.

    Obs. Não confunda com o metodo reverse(), o reverse só funciona em Listas. 
    Podemos usar o Reversed para reverter qualquer iterável.

    Ele retorna um reverse_iterator, que pode ser convertido para listas, tuplas ou outros iteráveis.
'''

lista = [1, 2, 3, 4, 5]
reversed = reversed(lista)
print(list(reversed), tuple(reversed), set(reversed))
print(type(reversed))