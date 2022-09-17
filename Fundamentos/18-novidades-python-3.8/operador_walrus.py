'''
    O Operador Walrus permite fazer atribuição e retorno do valor em uma unica expressão.
    
    variavel := expressao
'''

# Modo usual
nome = 'Pedro Henrique'
print(nome)

# Usando operador Walrus
print(nome := 'Pedro Henrique')


# Exemplo de lógica no modo usual
# cesta = []
# fruta = input('Informe a fruta: ')
# while fruta != 'jaca':
#     cesta.append(fruta)
#     fruta = input('Informe a fruta: ')

# Exemplo de lógica usando operador Walrus
cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)