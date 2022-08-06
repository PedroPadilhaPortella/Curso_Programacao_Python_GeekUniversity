'''
Assert -> Checa a validade de uma afirmação

Quando um script python é executado com a flag "-o", todos os asserts serão ignorados.
'''

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0
    return a + b

def comer_saudavel(comida):
    assert comida in ['vegatais', 'frutas', 'legumes']
    return f'Eu como {comida}'