'''

Tipos básicos: int, float, boolean, string, List, Set, Dict...
    Ex:
    def dobro(valor: int) -> int:
        return valor * 2

    print(dobro(4))
    print(dobro('Geek'))


Novos Tipos Precisos: 
    Literal Type
    Union
    Final
    TypedDict

'''
from typing import Literal, Union, Final, final, TypedDict


# Literal -> semelhante a um tipo Enum
def calculadora(valor1: int, valor2: int, operacao: Literal['+', '-', '*', '/'])-> None:
    if(operacao == '+'):
        print(valor1 + valor2)
    elif(operacao == '-'):
        print(valor1 - valor2)
    elif(operacao == '*'):
        print(valor1 * valor2)
    elif(operacao == '/'):
        print(valor1 / valor2)
    else:
        print('Erro')

calculadora(4, 5, '+')


# Union -> Permite a criação de atributos que possuem mais de uma possibilidade de tipo
def soma(valor1: int, valor2: int)-> Union[float, int]:
    return valor1 + valor2

print(soma(4, 3.2))


# Final -> Campos ou classes finais
NOME: Final = 'Pedro Portella'
print(NOME)

@final
class Pessoa:
    pass

# Base class "Pessoa" is marked final and cannot be subclassedPylance:
# class Estudante(Pessoa):
#     pass


# TypedDict -> Gera classes que são convertidos para dicionarios
class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.5.1', atualizacao=2020)
print(geek)