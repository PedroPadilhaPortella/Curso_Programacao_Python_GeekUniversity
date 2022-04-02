'''
    Objetos são as instâncias de classes.
    Encapsulamento e Abstração
'''

class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        Conta.contador += 1
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'CC {self.__numero}: Titular: {self.__titular}; Saldo: R$ {self.__saldo}; Limite: R$ {self.__limite}')

    def depositar(self, valor):
        if(valor < 0):
            print('O valor precisa ser positivo!')
            return False
        else:
            self.__saldo += valor
            print('Depósito Efetuado!')
            return True

    def sacar(self, valor):
        if(valor < 0):
            print('O valor precisa ser positivo!')
        elif(valor > self.__saldo):
            print('Saldo Insulficiente!')
        elif(valor > self.__limite):
            print('Valor acima do limite!')
        else:
            self.__saldo -= valor
            print('Saque Efetuado!')
            return True
        return False

    def transferir(self, valor, destino):
        taxas = 0.05 # Taxa de Trasnferência
        total = valor + (valor * taxas)
        operacao = self.sacar(total)
        if(operacao):
            self.__saldo -= valor
            destino.depositar(valor)
            print('Transferência Efetuada!')



conta1 = Conta('João', 1000, 500)
conta2 = Conta('Pedro', 0, 500)

conta1.depositar(-300)
conta1.depositar(300)

conta1.sacar(-500)
conta1.sacar(10000)
conta1.sacar(501)
conta1.sacar(300)

conta1.transferir(300, conta2)

conta1.extrato()
conta2.extrato()