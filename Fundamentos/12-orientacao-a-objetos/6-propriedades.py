'''
Propriedades - 
    São semelhantes aos atributos, mas são mais utilizados para armazenar dados.
    Como se fossem Getters e Setters.

    O decorator @property permite que seja acessado diretamente pelo objeto. Como se fosse uma propriedade.
'''

class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor
        
    def saque(self, valor):
        self.saldo -= valor

    def deposita(self, valor):
        self.saldo += valor


conta1 = Conta('José', 1000, 1000)

print(conta1.titular)
print(conta1.numero)
print(conta1.saldo)

conta1.limite = 100
print(conta1.limite)