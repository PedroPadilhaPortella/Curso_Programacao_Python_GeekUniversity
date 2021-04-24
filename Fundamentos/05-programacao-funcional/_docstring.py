'''
Documentação de funções com DocStrings
'''

def soma(a = 0, b = 0):
    """
    Funcao que retorna a soma de dois valores numericos
    :param a: primeiro valor da soma (default = 0)
    :param b: segundo valor da soma (default = 0)
    :return: soma dos parametros
    """
    return a + b
    
help(soma)
print(soma.__doc__)