from equipamento import Equipamento

class Computador(Equipamento):
    def __init__(self, nome, preco, memoria, processador):
        super().__init__(nome, preco)
        self.__memoria = memoria
        self.__processador = processador

    @property
    def memoria(self):
        return self.__memoria

    @property
    def processador(self):
        return self.__processador

    def exibir(self):
        super().exibir()
        print(f'Memória: {self.memoria}, Processador: {self.processador}')