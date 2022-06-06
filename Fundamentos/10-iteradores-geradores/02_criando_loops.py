'''
Criando nossa versão dos Loops
'''

def _for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

numeros = [1, 2, 3, 4, 5]
nome = 'pedro'

_for(numeros)
_for(nome)