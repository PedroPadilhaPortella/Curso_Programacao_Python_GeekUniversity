"""
    Annotations -> As annotations servem para indicar quais são os parametros anotados e seus tipos.
"""
import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


print(circunferencia.__annotations__)
nome: str = 'Geek University'
peso: float = 67.9
ativo: bool = True

print([nome, peso, ativo])
print(__annotations__) # Objeto com as annotations globais do módulo



class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa(nome='Geek University', idade=37, peso=69.5)

print(f"Dicionario: {p.__dict__}")
# print(f"Andar Annotations {p.__annotations__}") #Não tem annotations
print(f"Init Annotations {p.__init__.__annotations__}")
print(f"Andar Annotations {p.andar.__annotations__}")