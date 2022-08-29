'''
    Podemos adicionar tipagem às funções Python utilizando type hints, 
    embora isso não impeça o programa de passar variáveis de tipos diferentes dos indicados.
'''

def cumprimentar(nome: str) -> str :
    return f"Olá {nome}"

print(cumprimentar('Pedro'))
