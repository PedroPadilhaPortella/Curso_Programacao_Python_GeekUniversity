'''
    Polimorfismo
'''

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        raise NotImplementedError('A classe precisa implementar esse metodo.')

    def comer(self):
        raise NotImplementedError('A classe precisa implementar esse metodo.')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print('Au Au')

    def comer(self):
        print('Comendo ração')

class Gatos(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print('Miau')

    def comer(self):
        print('Beber leite')

class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print('Squeak')

    def comer(self):
        print('Comendo queijo')