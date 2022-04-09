class Equipamento:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    def exibir(self):
        print(f'Nome: {self.nome}, Preço: {self.preco}')