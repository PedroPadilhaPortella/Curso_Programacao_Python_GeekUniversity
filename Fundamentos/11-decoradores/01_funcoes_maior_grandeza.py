'''
Funções de Maior Grandeza - Higher-order Functions

    - Funções de maior grandeza são funções que recebem funções como argumentos e retornam funções.

    Quando em uma linguagem de programação temos high-order functions, indica que temos funções que podem receber como argumento e até retornar outras funções, ou criar variáveis do tipo Função. 

    Assim como em Javascript, em Python, as funções são cidadões de primeira classe, ou seja, podem ser atribuídas a variáveis, passadas como argumento, e retornadas como valor.
'''

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

# Função que recebe uma função como argumento
def calcular(funcao, a, b):
    return funcao(a, b)

print(calcular(somar, 10, 5))
print(calcular(subtrair, 10, 5))
print(calcular(multiplicar, 10, 5))
print(calcular(dividir, 10, 5))


'''
Nested Functions - Funções aninhadas

    Em Python podemos ter funções aninhadas, ou seja, funções dentro de funções.
    Nested Functions podem acessar o excopo das suas funções mais externas
'''
from random import choice

def cumprimentar(pessoa):
    def humor():
        return choice(('Opa bom dia ', 'Vai se foder ', 'Eae ' ))
    return humor() + pessoa

print(cumprimentar('Daniel'))


# Retornando fuções de outras funções, ou seja, só a referência da função, para ser executada posteriormente.
def faz_me_rir():
    risadas = ('kkk', 'hahaha', 'lol')
    def rir():
        return choice(risadas)
    return rir

tentar_rir = faz_me_rir()
print(tentar_rir())
print(faz_me_rir()())
